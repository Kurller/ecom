from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from .utils import cookieCart, cartData, guestOrder
from .models import *
import datetime
import json

# Create your views here.


def homeStore(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'home.html', context)


def productDetail(request, id):
    product = get_object_or_404(Product, id=id)
    photos = ProductImage.objects.filter(product=product)
    return render(request, 'detail.html', {'product': product, 'photos': photos})


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)


def checkOut(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('productID:', productID)
    print('action:', action)
    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Oboy, them don add the Item o', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['Form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['Shipping']['address'],
            city=data['Shipping']['city'],
            state=data['Shipping']['state'],
            zipcode=data['Shipping']['zipcode'],
        )
    return JsonResponse('Payment complete !', safe=False)

from django.urls import path
from estore import views

urlpatterns = [
    path('', views.homeStore, name='home'),
    path('<int:id>/', views.productDetail, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkOut, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]

from django.contrib import admin
from .models import *

# Register your models here.


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

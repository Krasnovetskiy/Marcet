from django.contrib import admin

from orders.models import Discount, Order, OrderItem


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('total_amount', 'user')


@admin.register(Discount)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(OrderItem)
class CategoryAdmin(admin.ModelAdmin):
    ...


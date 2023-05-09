from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    filter_horizontal = ('categories', 'products')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
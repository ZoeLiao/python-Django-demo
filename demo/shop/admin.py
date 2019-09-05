from django.contrib import admin
from shop.models import (
    Category,
    Product
)


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    # prepopulated_fields: 要使用其他字段來自動賦值的字段
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'stock',
        'available',
        'created_at',
        'updated_at'
    ]
    list_filter = [
        'available',
        'created_at',
        'updated_at'
    ]
    list_editable = [
        'price',
        'stock',
        'available'
    ]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

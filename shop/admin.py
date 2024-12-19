from django.contrib import admin
from .models import Category, Product, Tag, ProductDetail

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'uuid', 'price', 'stock', 'category', 'created_at')
    search_fields = ('name', 'slug', 'uuid')
    list_filter = ('category', 'created_at')

admin.site.register(Product,ProductAdmin)

admin.site.register(Tag)
admin.site.register(ProductDetail)
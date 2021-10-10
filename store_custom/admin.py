from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
# Register your models here.

class TagInline(GenericTabularInline):
    autocomplete_fields=['tag']
    extra=0
    min_num=1
    max_num=5
    model=TaggedItem

class CustomProductAdmin(ProductAdmin):
    inlines=[TagInline]
admin.site.unregister(Product)
admin.site.register(Product,CustomProductAdmin)
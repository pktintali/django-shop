from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','unit_price','inventory_status','collection_title']
    list_editable = ['unit_price']
    list_per_page=10
    list_select_related=['collection']

    def collection_title(self,Product):
        Product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self,Product):
        if Product.inventory<10:
            return 'Low'
        else:
            return 'Ok'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','membership']
    list_editable=['membership']
    ordering=['first_name','last_name']
    list_per_page=10

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','placed_at','customer']
    list_per_page=10
    list_select_related=['customer']

admin.site.register(models.Collection)
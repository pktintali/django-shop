from django.contrib import admin,messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.html import format_html,urlencode
from . import models
# Register your models here.

class InventoryFilter(admin.SimpleListFilter):
    title='inventory'
    parameter_name='inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low'),

        ]
    def queryset(self, request, queryset:QuerySet):
        if self.value()=='<10':
            return queryset.filter(inventory__lt=10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # fields=['title','slug']
    # exclude=['promotions']
    autocomplete_fields=['collection']
    prepopulated_fields={
        'slug':['title']
    }
    actions=['clear_inventory']
    list_display=['title','unit_price','inventory_status','collection']
    list_editable = ['unit_price']
    list_filter=['collection','last_update',InventoryFilter]
    list_per_page=10
    # list_select_related=['collection']

    # def collection_title(self,Product):
    #     Product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self,Product):
        if Product.inventory<10:
            return 'Low'
        else:
            return 'Ok'
    @admin.action(description='Clear Inventory')
    def clear_inventory(self,request,queryset):
        updated_count = queryset.update(inventory= 0)
        self.message_user(
            request,
            f'{updated_count} products were updated successfully',
            messages.SUCCESS
        )
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','membership','orders_count']
    list_editable=['membership']
    list_per_page=10
    ordering=['first_name','last_name']
    search_fields=['first_name__istartswith','last_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders_count(self,Customer):
        url = (reverse('admin:store_order_changelist')
        +'?'
        +urlencode({
            'customer_id':str(Customer.id)
        }))
        return format_html('<a href = "{}">{}</a>',url,Customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields=['customer']
    list_display=['id','placed_at','customer']
    list_per_page=10
    list_select_related=['customer']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','products_count']
    list_per_page=10
    search_fields=['title']
    @admin.display(ordering='products_count')
    def products_count(self,Collection):
        # reverse('admin:app_model_page')
        url = (reverse('admin:store_product_changelist')
        +'?'
        +urlencode({
            'collection__id':str(Collection.id)
        }))
        return format_html('<a href = "{}">{}</a>',url,Collection.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate( 
            products_count=Count('product')
        )
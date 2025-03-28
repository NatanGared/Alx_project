from django.contrib import admin
from .models import (
    Category,
    Item,
    Size,
    Supplier,
    Customer,
    PriceHistory,
    IncomingItem,
    Order,
    #Status,
    #User,
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')
    search_fields = ('category_name',)
    list_filter = ('category_name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'initial_price', 'category')
    search_fields = ('item_name',)
    list_filter = ('category',) 

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size_name', 'symbol','description')
    search_fields = ('size_name',)
    list_filter = ('symbol',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_person', 'phone_number', 'email')
    search_fields = ('company_name', 'contact_person')
    list_filter = ('company_name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email')
    search_fields = ('full_name',)
    list_filter = ('full_name',)

@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('item', 'size', 'price', 'effective_date')
    search_fields = ('item__item_name',)
    list_filter = ('item', 'size', 'effective_date')

@admin.register(IncomingItem)
class IncomingItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'size', 'quantity_received', 'date_received', 'supplier')
    search_fields = ('item__item_name',)
    list_filter = ('supplier', 'date_received') 

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'item', 'customer', 'quantity', 'price', 'status')
    search_fields = ('customer__full_name',)
    list_filter = ('status', 'item', 'customer')  
"""
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', 'description')
    search_fields = ('status_name',)
    list_filter = ('status_name',)

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'status')
    search_fields = ('user_name',)
    list_filter = ('status',)
"""
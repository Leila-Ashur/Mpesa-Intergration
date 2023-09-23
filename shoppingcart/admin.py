from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'calculate_total_price')
    list_filter = ('user',)
    search_fields = ('user__username', 'created_at')
    date_hierarchy = 'created_at'

    def calculate_total_price(self, obj):
        return obj.total_price()

    calculate_total_price.short_description = 'Total Price'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product_name', 'quantity', 'price', 'total_item_price')
    list_filter = ('cart__user', 'product_name')
    search_fields = ('cart__user__username', 'product_name')

    def total_item_price(self, obj):
        return obj.total_price()

    total_item_price.short_description = 'Total Item Price'

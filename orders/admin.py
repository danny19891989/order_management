from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'customer', 'total_amount', 'total_price', 'created_at']
    list_filter = ['created_at', 'total_price']
    search_fields = ['product_name', 'customer__username']

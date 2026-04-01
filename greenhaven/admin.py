from django.contrib import admin
from .models import Customer, Plant, Cart, Cart_Item, Order

admin.site.register(Customer)
admin.site.register(Plant)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'created_at', 'updated_at']

admin.site.register(Cart_Item)
admin.site.register(Order)
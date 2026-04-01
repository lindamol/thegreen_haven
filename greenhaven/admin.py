from django.contrib import admin
from .models import Customer, Plant, Cart, Cart_Item, Order

admin.site.register(Customer)
admin.site.register(Plant)
admin.site.register(Cart)
admin.site.register(Cart_Item)
admin.site.register(Order)  # ✅ NEW
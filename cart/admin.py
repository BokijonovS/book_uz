from django.contrib import admin

from .models import Order, OrderItem, Customer

# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

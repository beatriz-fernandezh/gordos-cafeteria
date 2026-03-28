from django.contrib import admin
from .models import Producto, Order, OrderItem

admin.site.register(Producto)
admin.site.register(Order)
admin.site.register(OrderItem)
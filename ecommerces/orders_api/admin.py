from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields] 
    list_editable = ['status','complete']
    list_filter = ['status']
    search_fields = ['status']
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
    list_filter = ['product']
    search_fields = ['product__name']
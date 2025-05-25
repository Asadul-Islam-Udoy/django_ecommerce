from django.contrib import admin
from .models import Product,ProductImage
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['image_preview']
    
    def image_preview(self,obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100"/>'
        return ""
    image_preview.allow_tags=True
    image_preview.short_description ="Preview"
    
@admin.register(Product)   
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','description','in_stock','discount_percent','discount_price','created_at']
    list_editable = ['name','price','description','in_stock','discount_percent']
    readonly_fields = ['discount_price']
    search_fields = ['name','description']
    list_filter = ['created_at']
    def discount_price(self,obj):
            return obj.discount_price
    discount_price.short_description = 'Discounted Price'
    inlines = [ProductImageInline]
    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id','product_id','image','uploaded_at']
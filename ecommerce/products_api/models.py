from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    description = models.CharField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class ProductImage(models.Model):
    product_id = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
from django.db import models
from products_api.models import Product
from users_api.models import CustomUser
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'), 
    ]
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def is_completed(self):
            return self.status == 'completed'
        
    def __str__(self):
        return f"Oder #{self.pk} by {self.customer.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
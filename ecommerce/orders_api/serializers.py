from  rest_framework import serializers
from products_api.models import Product
from users_api.models import CustomUser
from .models import Order,OrderItem
from products_api.serializers import ProductSerializer
from users_api.serializers import CustomSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset = Product.objects.all(),write_only=True, source='product'
    )
    class Meta:
        model = OrderItem
        fields = ['id','product','product_id','quantity']
        
class OrderSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True)
    customer = CustomSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset = CustomUser.objects.all(),write_only=True,source='customer'
    )
    class Meta:
        model = Order
        fields = ['id','customer','customer_id','date_ordered','complete','items']
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            
            if product.in_stock < quantity:
                raise serializers.ValidationError(
                    f"Not enough stock for product {product.name}"
                )
            product.in_stock -= quantity
            product.save()
            
            OrderItem.objects.create(order=order,product=product,quantity=quantity)
        return order

from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from .serializers import ProductImageSerializer,ProductSerializer
from .models import Product,ProductImage
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=True,methods=['post'])
    def upload_images(self,request,pk=None):
        product = self.get_object()
        files = request.FILES.getlist('images')
        for file in files:
            ProductImage.objects.create(product=product,image=file)
            
        return Response({'status':'image uploaded'},status=status.HTTP_201_CREATED)
    
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order
from users_api.permissions import IsSelfOfAdmin
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsSelfOfAdmin]
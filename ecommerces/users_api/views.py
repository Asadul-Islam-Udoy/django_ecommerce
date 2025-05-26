from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomSerializer,CustomTokenObtainPairSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
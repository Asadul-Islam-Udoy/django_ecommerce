from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomSerializer,CustomTokenObtainPairSerializer
from .permissions import IsSelfOfAdmin
from rest_framework import viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer
    permission_classes = [IsSelfOfAdmin]
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
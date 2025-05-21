from rest_framework.routers import DefaultRouter
from .views import UserViewSet,CustomTokenObtainPairView
from django.urls import path
router = DefaultRouter(trailing_slash=False)
router.register(r'users',UserViewSet)
urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/',CustomTokenObtainPairView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls

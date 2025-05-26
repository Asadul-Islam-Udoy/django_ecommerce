from .views import OrderViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash=False)

router.register(r'orders',OrderViewSet)

urlpatterns = router.urls

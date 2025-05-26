from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
router = DefaultRouter(trailing_slash=False)

router.register(r'products',ProductViewSet)

urlpatterns = router.urls

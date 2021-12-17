from rest_framework import routers, urlpatterns
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet, basename='products')

urlpatterns = []

urlpatterns += router.urls
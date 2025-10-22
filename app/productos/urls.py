from .views import ProductoAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ProductoAPIView, basename='productos')
urlpatterns = router.urls
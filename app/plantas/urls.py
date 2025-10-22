from .views import PlantasApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', PlantasApiView, basename='plantas')
urlpatterns = router.urls

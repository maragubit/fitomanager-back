
from .views import IndicacionesAPIView
from rest_framework.routers import DefaultRouter
from .views import DepartamentoIndicacionesAPIView

router=DefaultRouter()
router.register(r'indicaciones', IndicacionesAPIView, basename='indicaciones')
router.register(r'departamentos', DepartamentoIndicacionesAPIView, basename='departamentos')
urlpatterns = router.urls
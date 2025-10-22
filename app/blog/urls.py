from django.urls import path
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', views.BlogApiView, basename='blog')
router.register(r'categories', views.CategoryApiView, basename='categories')

urlpatterns = [
    
    
    
]+ router.urls
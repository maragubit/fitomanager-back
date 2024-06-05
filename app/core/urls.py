from django.urls import path
from core import views
from .views import acercade, politicaprivacidad






urlpatterns = [
    
    path("", views.home , name="portada"),
    path("acercade",acercade.as_view(),name='acercade'),
    path("politicaprivacidad",politicaprivacidad.as_view(),name='politicaprivacidad'),
    
]
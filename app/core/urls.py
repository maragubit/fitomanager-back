from django.urls import path, re_path
from core import views
from .views import acercade, politicaprivacidad, redirigir_blog






urlpatterns = [
    
    path("", views.home , name="portada"),
    re_path(r"^blog/(?P<path>.*)$", redirigir_blog),
    path("acercade",acercade.as_view(),name='acercade'),
    path("politicaprivacidad",politicaprivacidad.as_view(),name='politicaprivacidad'),
    
]
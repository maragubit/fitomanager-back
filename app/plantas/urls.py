from django.urls import path
from .views import *
from . import views

urlpatterns = [
    #path modelo ficha
    path('',views.plantas, name= 'plantas'),
    path('planta/<int:pk>',PlantaUpdate.as_view(),name='plantasedit'),
    path('etiqueta/<int:pk>/', views.plantasetiqueta,name='listaetiqueta'),




]
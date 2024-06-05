from django.urls import path
from . import views
from .views import *
urlpatterns = [


    path('',PatologiasViews.as_view(), name="patologias"),
    path('<int:pk>', IndicacionesDetailView.as_view(),name='patologia'),
    path('buscarpatologia', views.buscadorpatologia,name='buscarpatologia'),
    path('departamento/<int:category_id>/', views.category,name='departamento'),

]
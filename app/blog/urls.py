from django.urls import path
from . import views
from .views import *
urlpatterns = [
    
    
    path('',blog.as_view(), name="blog"),
    path('category/<int:category_id>/', views.category,name='category'),
    path('entrada/<int:pk>/', BlogDetailView.as_view(),name='entrada'),
    path('entrada/buscarblog/', views.buscadorblog,name='buscarblog'),
    path('subcategory/<int:subcategory_id>/', views.subcategory,name='subcategory'),
]
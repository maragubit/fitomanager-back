from django.urls import path
from productos import views
from .views import ProductoDetailView, ProductosViews, comparador
urlpatterns = [
    path('producto/<int:pk>/', ProductoDetailView.as_view(),name='producto'),
    path('', ProductosViews.as_view(),name='productos'),
    path('comparador', views.comparador,name='comparador'),
    path('filtrado', views.filtradoproductos,name='filtrador'),
    path('buscarproducto', views.buscadorproducto,name='buscarproducto'),
]
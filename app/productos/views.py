from plantas.serializers import PlantaSerializer
from .models import Producto
from plantas.models import Planta
from productos.serializers import ProductoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
from rest_framework import status
from django.db.models import Q

class ProductoAPIView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) |
                Q(plantas__indicaciones__sintomas__icontains=search)
            )

        return queryset.distinct()
    
    @swagger_auto_schema(
        method='get',
        operation_summary="Devuelve las 3 últimos productos añadidos",
        operation_description="API para devolver las 3 productos añadidas",
        responses={200: ProductoSerializer(many=True)},
    )
    @action(detail=False, methods=["get"], url_path='productoHome')
    def productoHome(self, request):
        productos = Producto.objects.filter(fitomanager=False).order_by('-id')[:4]
        productos = ProductoSerializer(productos, many=True,context={'request': request}).data
        return Response(productos)

    
    

    
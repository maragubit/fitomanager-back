from rest_framework import filters
from .models import Indicacion
from rest_framework import viewsets
from .serializers import IndicacionesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from .serializers import DepartamentoIndicacionesSerializer
from .models import Departamento

class IndicacionesAPIView(viewsets.ModelViewSet):
    queryset = Indicacion.objects.all()
    serializer_class = IndicacionesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Permitir acceso sin autenticación
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombre", "sintomas"]
    pagination_class = None 
    
    @swagger_auto_schema(
        method='get',
        operation_summary="Devuelve las 3 últimas indicaciones añadidas",
        operation_description="API para devolver las 3 indicaciones añadidas",
        responses={200: IndicacionesSerializer(many=True)},
        tags=['indicaciones']
    )
    @action(detail=False, methods=['get'], url_path='indicacionesHome')
    def indicacionesHome(self,request):
        indicaciones = Indicacion.objects.exclude(modo_oculto="si").order_by('-id').first()
        serializer = IndicacionesSerializer(indicaciones, context={'request': request})
        return Response(serializer.data)
    
class DepartamentoIndicacionesAPIView(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoIndicacionesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Permitir acceso sin autenticación
    pagination_class = None 
    
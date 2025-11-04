from django.shortcuts import render
from django.urls import reverse_lazy

from plantas.serializers import PlantaSerializer
from plantas.serializers import PlantaIndicacionesSerializer
from .models import Planta
from indicaciones.models import Indicacion
from indicaciones.models import Departamento
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core import serializers
from text_unidecode import unidecode
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters

# Create your views here.


#-----------------Modelo ficha-------------------------------


class PlantasApiView(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # solo lectura
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombre", "especie"]

    @swagger_auto_schema(
        method='get',
        operation_summary="Devuelve las 3 últimas plantas añadidas",
        operation_description="API para devolver las 3 plantas añadidas",
        responses={200: PlantaSerializer(many=True)},
        tags=['plantas']
    )
    @action(detail=False, methods=["get"], url_path='plantasHome')
    def plantasHome(self, request):
        plantas = Planta.objects.all().order_by('-id')[:3]
        plantas = PlantaSerializer(plantas, many=True,context={'request': request}).data
        return JsonResponse(plantas, safe=False)
    
    
    @action(detail=False, methods=["get"], url_path='plantasTotal')
    def plantasTotal(self, request):
        self.pagination_class = None
        plantas = Planta.objects.all()
        plantas = PlantaSerializer(plantas, many=True,context={'request': request}).data
        return JsonResponse(plantas, safe=False)
    
from django.shortcuts import render
from django.urls import reverse_lazy
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



# Create your views here.


#-----------------Modelo ficha-------------------------------


def plantas(request):
    plantas=Planta.objects.all().order_by('nombre')
    indicaciones=Indicacion.objects.all()
    plantasjson=serializers.serialize('json',plantas)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        patologia=request.POST.get('patologia')
        value=request.POST.get('value')
        from text_unidecode import unidecode
        for planta in Planta.objects.all():
            planta.nombre=unidecode(u'{}'.format(planta.nombre)).lower()
            planta.especie=unidecode(u'{}'.format(planta.especie)).lower()
            value=unidecode(u'{}'.format(value).lower())
            plantas_list= Planta.objects.filter(nombre__contains=value)|Planta.objects.filter(especie__contains=value)|Planta.objects.filter(activos__contains=value)|Planta.objects.filter(usos__contains=value)
            plantas_list=plantas_list.order_by('nombre')
            if patologia != 'todas':
                plantas_list=plantas_list.filter(indicaciones__id=patologia)
            plantasjs=serializers.serialize('json',plantas_list)
            return JsonResponse(data={'plantasjs': plantasjs})
        else:
            plantas_list=Planta.objects.filter(nombre__contains=value).order_by('nombre')|Planta.objects.filter(especie__contains=value).order_by('nombre')|Planta.objects.filter(activos__contains=value).order_by('nombre')|Planta.objects.filter(usos__contains=value).order_by('nombre')
            if patologia != 'todas':
                plantas_list=plantas_list.filter(indicaciones__id=patologia)
            plantasjs=serializers.serialize('json',plantas_list)
            return JsonResponse(data={'plantasjs': plantasjs})
    return render(request,'plantas/plantaslist.html',{'plantasjson':plantasjson, 'indicaciones':indicaciones})






class PlantaUpdate(UpdateView):
    model = Planta
    template_name = "plantas/plantasedit.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):  # método para que aparezcan los votos y las estrellas en la puntuación:
        context = super().get_context_data(**kwargs)
        productos = self.object.plantasproducto.all()[:4]
        context['productos'] = productos
        return context



def plantasetiqueta(request,**kwargs):
    plantas=Planta.objects.filter(etiquetas=kwargs['pk'])
    return render (request,'plantas/plantaslistetiqueta.html',{'plantas':plantas})

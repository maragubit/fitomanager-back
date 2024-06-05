from django.shortcuts import render, get_object_or_404
from .models import Indicacion, Departamento
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core import serializers
from decimal import *
from productos.models import Producto

# Create your views here.
class PatologiasViews(ListView):
    model = Indicacion
    template_name = "indicaciones/patologias.html"
    paginate_by = 9
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Departamento.objects.all()
        context['categories'] = categories
        return context

class IndicacionesDetailView(DetailView):

    model = Indicacion
    template_name = 'indicaciones/patologia.html'


    def get_context_data(self, **kwargs):  # método para que aparezcan los votos y las estrellas en la puntuación:
        context = super().get_context_data(**kwargs)
        productos_list=[]
        productos= Producto.objects.filter(evidencias__indicacion=self.object)
        for producto in productos[:4]:
            productos_list.append(producto)
        for producto in productos:
            for evidencia in producto.evidencias.all():
                if evidencia.indicacion == self.object: #vamos a ver la nota del producto para esta enfermedad
                    if not productos_list:
                        productos_list.append(producto) #si la lista vacía, añadimos el productos
                    else:
                        for evidencia1 in productos_list[0].evidencias.all(): #si no vacia, comparamos con el primero
                            if evidencia1.indicacion == self.object:
                                media=Decimal((evidencia.nota*8)+(producto.estandarizacion)+(producto.laboratorio))/10+(producto.puntoextra)/2
                                media1=Decimal((evidencia1.nota*8)+(productos_list[0].estandarizacion)+(productos_list[0].laboratorio))/10+productos_list[0].puntoextra/2
                                if media == media1:
                                    if producto.pvp<productos_list[0].pvp:
                                        productos_list.insert(0,producto)
                                elif media> media1:
                                    productos_list.insert(0,producto)

                                else:
                                    for evidencia1 in productos_list[1].evidencias.all(): #si no vacia, comparamos con el segundo
                                        if evidencia1.indicacion == self.object:
                                            media=Decimal((evidencia.nota*8)+(producto.estandarizacion)+(producto.laboratorio))/10+(producto.puntoextra)/2
                                            media1=Decimal((evidencia1.nota*8)+(productos_list[1].estandarizacion)+(productos_list[1].laboratorio))/10+productos_list[1].puntoextra/2
                                            if media == media1:
                                                if producto.pvp < productos_list[1].pvp:
                                                    productos_list.insert(1,producto)
                                            elif media> media1:
                                                productos_list.insert(1,producto)
                                            else:
                                                for evidencia1 in productos_list[2].evidencias.all(): #si no vacia, comparamos con el tercero
                                                    if evidencia1.indicacion == self.object:
                                                        media=Decimal((evidencia.nota*8)+(producto.estandarizacion)+(producto.laboratorio))/10+(producto.puntoextra)/2
                                                        media1=Decimal((evidencia1.nota*8)+(productos_list[2].estandarizacion)+(productos_list[2].laboratorio))/10+productos_list[2].puntoextra/2
                                                        if media == media1:
                                                            if producto.pvp < productos_list[2].pvp:
                                                                    productos_list.insert(2,producto)
                                                        elif media> media1:
                                                            productos_list.insert(2,producto)
                                                        else:
                                                            for evidencia1 in productos_list[3].evidencias.all(): #si no vacia, comparamos con el cuarto
                                                                if evidencia1.indicacion == self.object:
                                                                    media=Decimal((evidencia.nota*8)+(producto.estandarizacion)+(producto.laboratorio))/10+(producto.puntoextra)/2
                                                                    media1=Decimal((evidencia1.nota*8)+(productos_list[3].estandarizacion)+(productos_list[3].laboratorio))/10+(productos_list[3].puntoextra)/2
                                                                    if media == media1:
                                                                        if producto.pvp < productos_list[3].pvp:
                                                                            productos_list.insert(3,producto)
                                                                    elif media> media1:
                                                                        productos_list.insert(3,producto)
        productos_list=productos_list[:4]
        productosjson=serializers.serialize('json',productos_list)
        context['productos'] = productos_list
        context['productosjson'] = productosjson
        return context


def category(request, category_id):
    category = get_object_or_404(Departamento, id= category_id)
    categories=Departamento.objects.all()
    return render(request,"indicaciones/departamentopatologias.html",{'category': category,'categories':categories})

def buscadorpatologia(request,*args,**kwargs):
    from text_unidecode import unidecode
    patologiasid=[]
    for indicacion in Indicacion.objects.all():
        indicacion.nombre=unidecode(u'{}'.format(indicacion.nombre)).lower()
        indicacion.sintomas=unidecode(u'{}'.format(indicacion.sintomas)).lower()
        busqueda=unidecode(u'{}'.format(request.POST.get('buscador'))).lower()
        if busqueda in indicacion.nombre or busqueda in indicacion.sintomas:
            if indicacion.id not in patologiasid:
                patologiasid.append(indicacion.id)


    patologias= Indicacion.objects.filter(id__in=patologiasid)
    return render (request,"indicaciones/buscarindicaciones.html",{'patologias':patologias})
from .models import Producto
from django.views.generic import DetailView
from django.shortcuts import render
from django.views.generic import ListView
from .forms import ProductoForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core import serializers


class ProductoDetailView(DetailView):

    model = Producto
    template_name = 'productos/producto.html'
    def get_context_data(self, **kwargs):  # método para que aparezcan los votos y las estrellas en la puntuación:
        context = super().get_context_data(**kwargs)
        producto=self.object.evidencias.all()
        evidenciasjson=serializers.serialize('json',producto)
        if self.object.puntoextra:
            puntoextra=self.object.puntoextra
        else:
            puntoextra=0
        context['evidenciasjson'] = evidenciasjson
        context['puntoextra'] = puntoextra
        return context

class ProductosViews(ListView):
    model = Producto
    template_name = "productos/productoslist.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):  # método para que aparezcan los votos y las estrellas en la puntuación:
        context = super().get_context_data(**kwargs)
        form = ProductoForm()
        context['form'] = form
        return context





def comparador(request):
    idlist=request.POST.getlist('seleccion[]')
    if len(idlist)<=10 and len(idlist)>=2:
        productos= Producto.objects.filter(id__in=idlist)
        return render (request, "productos/comparador.html",{'productos':productos})
    else:
        return render (request, "productos/comparador.html")

def filtradoproductos(request):
    from indicaciones.models import Indicacion
    from plantas.models import Planta
    plantas= request.POST.get('plantas')
    indicaciones= request.POST.get('indicaciones')
    if plantas=='' and indicaciones!='':
        object_list=Producto.objects.filter(indicaciones__id=indicaciones)
    if plantas !='' and indicaciones=='':
        object_list=Producto.objects.filter(plantas__id=plantas)
    if plantas =='' and indicaciones=='':
        object_list=Producto.objects.all()
    if plantas !='' and indicaciones !='':
        object_list=Producto.objects.filter(plantas__id=plantas, indicaciones__id=indicaciones)

    if indicaciones !='':
        indicacion=Indicacion.objects.get(id=indicaciones)

    else:
        indicacion=None

    if plantas !='':
        planta=Planta.objects.get(id=plantas)
    else:
        planta=None

    form=ProductoForm
    return render (request, "productos/filtrado.html",{'object_list':object_list,'form':form,'planta':planta,'indicacion':indicacion})

def buscadorproducto(request,*args,**kwargs):
    from text_unidecode import unidecode
    patologiasid=[]
    for indicacion in Producto.objects.all():
        indicacion.nombre=unidecode(u'{}'.format(indicacion.nombre)).lower()
        busqueda=unidecode(u'{}'.format(request.POST.get('buscador'))).lower()
        if busqueda in indicacion.nombre:
            if indicacion.id not in patologiasid:
                patologiasid.append(indicacion.id)

    form=ProductoForm
    productos= Producto.objects.filter(id__in=patologiasid)
    return render (request,"productos/buscarproductos.html",{'object_list':productos,'form':form,'busqueda':request.POST.get('buscador')})
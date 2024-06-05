from django.shortcuts import render
from plantas.models import Planta
from indicaciones.models import Indicacion
from blog.models import Post
from productos.models import Producto
from django.views.generic import TemplateView
from productos.models import Producto

# Create your views here.

def home(request):
    plantaquery=Planta.objects.all().order_by('-pk')[:1]
    listablog = Post.objects.all().order_by('-created')[:2]
    listaplantas = Planta.objects.all().order_by('-pk')[:3]
    indicaciones = Indicacion.objects.all().order_by('-pk')[:4]
    productos = Producto.objects.all().order_by('-pk')[:8]
    return render(request,"core/portada.html",{'listaplantas':listaplantas,'plantaquery':plantaquery,'listablog':listablog,'indicaciones':indicaciones, 'productos':productos})

class acercade(TemplateView):
    template_name = "core/acercade.html"


class politicaprivacidad(TemplateView):
    template_name = "core/politicaprivacidad.html"

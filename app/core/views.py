from django.shortcuts import redirect, render
from plantas.models import Planta
from indicaciones.models import Indicacion
from blog.models import Post
from productos.models import Producto
from django.views.generic import TemplateView
from productos.models import Producto
import re

# Create your views here.

def home(request):
    return render(request,"core/portada.html")

def redirigir_blog(request, path=None):
    return redirect(f"https://www.fitomanager.com/blog/{path}")

class acercade(TemplateView):
    template_name = "core/acercade.html"


class politicaprivacidad(TemplateView):
    template_name = "core/politicaprivacidad.html"

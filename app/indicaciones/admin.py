from django.contrib import admin
from .models import Indicacion, Departamento
from plantas.models import Planta

# Register your models here.
class PlantaInline(admin.TabularInline):
    model = Planta.indicaciones.through

class IndicacionAdmin(admin.ModelAdmin):
    inlines = [
        PlantaInline,
    ]

admin.site.register(Indicacion,IndicacionAdmin)
admin.site.register(Departamento)


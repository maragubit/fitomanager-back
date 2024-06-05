from django.contrib import admin
from .models import Planta,Evidencia

# Register your models here.
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('nombre','dosis_efectiva',)
admin.site.register(Planta,PlantaAdmin)
admin.site.site_title = "FitoManager"
admin.site.site_header = "FitoManager"
admin.site.register(Evidencia)
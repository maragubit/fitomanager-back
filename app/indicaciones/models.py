from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Departamento(models.Model):
    name=models.CharField(verbose_name="Nombre categoria", max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    logo=models.ImageField(upload_to='departamento')
    class Meta:
        verbose_name="Departamento"
        verbose_name_plural="Departamentos"
        ordering=['name']

    def __str__(self):
        return self.name

class Indicacion(models.Model):
    OCULTO_CHOICES=(
        ('si','si'),
        ('no','no'),
    )
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = RichTextField(blank=True,null=True)
    fisiopatologia = RichTextField(blank=True,null=True)
    imagen = models.ImageField(upload_to='indicacion',blank=True,null=True)
    fitoterapia= RichTextField(blank=True,null=True)
    sintomas= models.TextField(blank=True, null=True)
    categories=models.ManyToManyField(Departamento,verbose_name="Categoría",related_name="get_posts", blank=True)
    modo_oculto=models.CharField(choices=OCULTO_CHOICES,default='no', max_length=30)



    def __str__(self):
        return self.nombre

    class Meta():
        ordering = ['nombre']
        verbose_name_plural= 'indicaciones'
        
    def get_products(self):
        from plantas.models import Planta
        plantas=Planta.objects.filter(indicaciones__id=self.id)
        queryset = list({product for planta in plantas for product in planta.productos.all()})
        return queryset

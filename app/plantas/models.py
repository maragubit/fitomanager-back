from django.db import models
from indicaciones.models import Indicacion
from productos.models import Producto
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.
class Planta(models.Model):
    EMBARAZO_CHOICES = (
    ('SI','Su empleo es seguro'),
    ('NO','Su empleo no está recomendado'),
    ('BPM','Bajo prescripción médica')
    )

    LACTANCIA_CHOICES = (
    ('SI','Su empleo es seguro'),
    ('NO','Su empleo no está recomendado'),
    ('BPM','Bajo prescripción médica')
    )
  
    EDAD_CHOICES = (
    ('0','Cero meses'),
    ('2','Dos años'),
    ('3','Tres años'),
    ('4','Cuatro años'),
    ('6','Seis años'),
    ('10','Diez años'),
    ('12','Doce años'),
    ('16','16 años'),
    ('18','18 años'),
    )
    nombre = models.CharField(unique=True, max_length=100)
    droga = models.CharField(max_length=100,null=True,blank=True)
    especie = models.CharField(unique=True, max_length=100)
    posologia = RichTextField(blank=True,null=True)
    dosis_efectiva=models.DecimalField(blank=True,null=True, max_digits=5, decimal_places=2)
    activos = RichTextField(blank=True,null=True)
    mecanismo = RichTextField(blank=True, null=True)
    indicaciones = models.ManyToManyField('indicaciones.Indicacion',related_name='indicacionplanta',blank=True)
    evidencias= models.ManyToManyField('plantas.Evidencia', related_name='plantas',blank=True)
    contraindicaciones = RichTextField(blank=True, null=True)
    interacciones = RichTextField(blank=True, null=True)
    embarazo=models.CharField(max_length=5, choices=EMBARAZO_CHOICES, default='NO')
    lactancia=models.CharField(max_length=5, choices=LACTANCIA_CHOICES, default='NO')
    edad= models.CharField(max_length=5, choices=EDAD_CHOICES, default='12')
    imagen = models.ImageField(upload_to='plantas',blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    usos = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.nombre
    
    class Meta():
        ordering = ['nombre']



class Evidencia(models.Model):

    NOTA_CHOICES=(
        (1,'uno'),
        (2,'dos'),
        (3,'tres'),
        (4,'cuatro'),
        (5,'cinco'),
    )

    indicacion=models.ForeignKey('indicaciones.Indicacion',related_name='evidencias', on_delete=models.CASCADE)
    nota=models.IntegerField(choices=NOTA_CHOICES)

    def __str__(self):
        return ('{}: {}').format(self.indicacion.nombre,self.nota)

    class Meta():
        ordering = ['indicacion']
from unittest import case
from django.db import models
from indicaciones.models import Indicacion
from productos.models import Producto
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from PIL import Image
import io
from django.core.files.base import ContentFile
import os

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
    indicaciones = models.ManyToManyField('indicaciones.Indicacion',related_name='plantas',blank=True)
    evidencias= models.ManyToManyField('plantas.Evidencia', related_name='plantas',blank=True)
    contraindicaciones = RichTextField(blank=True, null=True)
    interacciones = RichTextField(blank=True, null=True)
    embarazo=models.CharField(max_length=5, choices=EMBARAZO_CHOICES, default='NO')
    lactancia=models.CharField(max_length=5, choices=LACTANCIA_CHOICES, default='NO')
    edad= models.CharField(max_length=5, choices=EDAD_CHOICES, default='12')
    imagen = models.ImageField(upload_to='plantas',blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    usos = models.TextField(blank=True, null=True)
    
    class Meta():
            ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagen:
            img_path = self.imagen.path
            img = Image.open(img_path)

            # Convertir a RGB si tiene alpha (transparencia)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Crear nombre nuevo
            webp_name = os.path.splitext(self.imagen.name)[0] + ".webp"
            buffer = io.BytesIO()
            img.save(buffer, format='WEBP', quality=85)

            # Sobrescribir imagen con versión WebP
            self.imagen.save(webp_name, ContentFile(buffer.getvalue()), save=False)
            os.remove(img_path)  # Eliminar el archivo original

            super().save(update_fields=['imagen'])  # Guardar con la nueva imagen
    
    
    



class Evidencia(models.Model):

    NOTA_CHOICES=(
        (1,'uno'),
        (2,'dos'),
        (3,'tres'),
        (4,'cuatro'),
        (5,'cinco'),
        (0,'sin calificar'),
    )

    indicacion=models.ForeignKey('indicaciones.Indicacion',related_name='evidencias', on_delete=models.CASCADE)
    nota=models.IntegerField(choices=NOTA_CHOICES, default=0)

    def __str__(self):
        return ('{}: {}').format(self.indicacion.nombre,self.nota)
    
    def evidencia_texto(self):
        nota=self.nota
        match (nota):
            case 1:
                return 'Las evidencias indican que la planta no es eficaz'
            case 2:
                return 'No hay evidencias que indiquen que se pueda emplear'
            case 3:
                return 'El uso tradicional nos indica que la planta podría ser eficaz'
            case 4:
                return 'Los estudios científicos indican que probablemente sea eficaz'
            case 5:
                return 'Los estudios científicos han demostrado que la planta es eficaz'
            case _:
                return "planta pendiente de calificar para esta patología"

    class Meta():
        ordering = ['indicacion']
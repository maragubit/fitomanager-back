from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from plantas.models import *
from indicaciones.models import *
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Producto(models.Model):

    nombre= models.CharField(unique=True, max_length=100)
    descripcion= models.TextField(blank=True, null=True)
    plantas= models.ManyToManyField('plantas.Planta',related_name='plantasproducto',blank=True)
    indicaciones=models.ManyToManyField('indicaciones.Indicacion',blank=True, related_name='indicacionesproducto')
    composicion= RichTextField(blank=True,null=True)
    posologia=models.TextField(blank=True, null=True)
    dosis=models.ManyToManyField('productos.Dosisproducto',blank=True)
    foto= models.ImageField(upload_to='productos')
    linkamazon= models.URLField(blank=True, null=True)
    pvp_amazon=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    linkpromofarma=models.URLField(blank=True, null=True)
    pvp_promofarma=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    pvp= models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    valoracion=RichTextField(blank=True,null=True)
    laboratorio= models.PositiveIntegerField(blank=True, null=True,validators=[MinValueValidator(1), MaxValueValidator(5)],)
    estandarizacion= models.PositiveIntegerField(blank=True, null=True,validators=[MinValueValidator(1), MaxValueValidator(5)],)
    puntoextra= models.DecimalField(blank=True, null=True,validators=[MinValueValidator(0), MaxValueValidator(1)],max_digits=2, decimal_places=1)
    media2= models.DecimalField(blank=True, null=True,validators=[MinValueValidator(1), MaxValueValidator(11)],max_digits=3, decimal_places=1)
    evidencias= models.ManyToManyField('plantas.Evidencia', related_name='productos',blank=True)



    def __str__(self):
        return ('{}').format(self.nombre)

    class Meta():
        ordering = ['-media2','pvp']


    def save(self, *args, **kwargs):
        from decimal import Decimal
        super().save(*args, **kwargs)
        if self.dosis.all():
            for dosis in self.dosis.all():
                if dosis.dosis >= dosis.planta.dosis_efectiva:
                    for evidencia in dosis.planta.evidencias.all():
                        self.evidencias.add(evidencia)
                        self.indicaciones.add(evidencia.indicacion)

        if self.dosis.all() and not self.evidencias.all():
            if self.indicaciones.all():
                self.media2=((self.estandarizacion*0.1)+(self.laboratorio*0.1))*2
                if self.puntoextra:
                    self.media2=Decimal(self.media2) + self.puntoextra
                    if self.media2 > 10:
                        self.media2 = 10

        else:
            evidencias=[]
            for evidencia in self.evidencias.all():
                if evidencias:
                    for evidencia1 in evidencias:
                        if evidencia.nota>=evidencia1.nota:
                            evidencias.remove(evidencia1)
                            evidencias.append(evidencia)
                else:
                    evidencias.append(evidencia)
            for evidencia in evidencias:
                self.media2=((evidencia.nota*0.8)+(self.estandarizacion*0.1)+(self.laboratorio*0.1))*2
                if self.puntoextra:
                    self.media2=Decimal(self.media2) + self.puntoextra
                    if self.media2 > 10:
                         self.media2 = 10
            super().save(*args, **kwargs)

        if not self.dosis.all():
            self.media2=None
        if self.pvp_amazon is None:
            self.pvp_amazon=999
        if self.pvp_promofarma is None:
            print('es cero')
            self.pvp_promofarma=999

        if self.pvp_promofarma<=self.pvp_amazon:
            self.pvp=self.pvp_promofarma
        else:
            self.pvp=self.pvp_amazon
        if self.puntoextra is None:
            self.puntoextra=0

        super().save(*args, **kwargs)






class Dosisproducto(models.Model):
    planta=models.ForeignKey('plantas.Planta',on_delete=models.CASCADE,related_name='dosisproducto')
    dosis=models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return ('{}: {} gramos').format(self.planta, self.dosis)

    class Meta():
        ordering = ['planta']


from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from plantas.models import *
from indicaciones.models import *
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from .utils import scrapping_amazon_drasanvi, scrapping_amazon_solgar ,scrapping_amazon_soria, scrapping_amazon_biojoy
import requests
from bs4 import BeautifulSoup

# Create your models here.


class Producto(models.Model):
    lab_LIST=(
        ('Drasanvi','Drasanvi'),
        ('Soria','Soria'),
        ('Solgar','Solgar'),
        ('Biojoy','Biojoy'),
    )

    nombre= models.CharField(max_length=250, blank=True, null=True)
    autocomplete=models.BooleanField(default=True)
    fitomanager=models.BooleanField(default=False)
    descripcion= models.TextField(blank=True, null=True)
    plantas= models.ManyToManyField('plantas.Planta',related_name='productos',blank=True)
    composicion= RichTextField(blank=True,null=True)
    posologia=models.TextField(blank=True, null=True)
    imagen= models.ImageField(upload_to='productos/', blank=True, null=True)
    foto= models.URLField(blank=True, null=True)
    link=models.URLField(blank=True, null=True)
    pvp= models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    media= models.DecimalField(blank=True, null=True,validators=[MinValueValidator(1), MaxValueValidator(11)],max_digits=3, decimal_places=1)
    laboratorio= models.CharField(max_length=50, choices=lab_LIST, blank=True, null=True)
    
    class Meta():
        ordering = ['-id']

    def __str__(self):
        return ('{}').format(self.nombre)
    
    """ CAPTAR PVP DE PROMOFARMA"""
   """  def save(self, *args, **kwargs):
        if not self.link or self.fitomanager or not self.autocomplete:
            super(Producto, self).save(*args, **kwargs)
            return
        else:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/125.0.0.0 Safari/537.36"}
            html = requests.get(self.link, headers=headers).text
            soup = BeautifulSoup(html, "html.parser")
            self.nombre= soup.find("span", id="productTitle").text
        if (self.laboratorio=='Drasanvi'):
            data= scrapping_amazon_drasanvi(soup)
            self.descripcion= data['descripcion']
            self.composicion= data['composicion']
            self.posologia= data['posologia']
        if (self.laboratorio=='Solgar'):
            data= scrapping_amazon_solgar(soup)
            self.descripcion= data['descripcion']
            self.composicion= data['composicion']
            self.posologia= data['posologia']
        if (self.laboratorio=='Soria'):
            data= scrapping_amazon_soria(soup)
            self.descripcion= data['descripcion']
            self.composicion= data['composicion']
            self.posologia= data['posologia']
        if (self.laboratorio=='Biojoy'):
            data= scrapping_amazon_biojoy(soup)
            self.descripcion= self.nombre
            self.composicion= data['composicion']
            self.posologia= data['posologia']
        print(data)
        
        price_entero = soup.find("span", class_="a-price-whole").text
        price_decimal = soup.find("span", class_="a-price-fraction").text
        image = soup.find("img", id="landingImage")
        # Asegurarte de que existe antes de acceder al atributo
        self.foto = image["src"] if image and "src" in image.attrs else None
        price= price_entero + price_decimal
        
        if price:
            self.pvp = float(price.replace(",", ".").strip())
        else:
            self.pvp = 0
        super(Producto, self).save(*args, **kwargs) """

    





from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name=models.CharField(verbose_name="Nombre categoria", max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=['name']

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name=models.CharField(verbose_name="Nombre subcategoria", max_length=100)
    category= models.ForeignKey('blog.Category',on_delete=models.CASCADE, related_name='subcategory')
    class Meta:
        verbose_name="Subcategoria"
        verbose_name_plural="Subcategorias"
        ordering=['name']
    def __str__(self):
        return self.name

class Post(models.Model):
    title= models.CharField(max_length=200, verbose_name="Título")
    content=RichTextUploadingField(verbose_name="Entrada")
    published=models.DateTimeField(default=now,verbose_name="Fecha de publicación")
    image=models.ImageField(verbose_name="Imagen",upload_to='blog',null=True,blank=True)
    author=models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category,verbose_name="Categoría",related_name="get_posts")
    subcategories=models.ManyToManyField("SubCategory",verbose_name="Subcategoría",related_name="get_posts",blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering=['-created']

    def __str__(self):
        return self.title



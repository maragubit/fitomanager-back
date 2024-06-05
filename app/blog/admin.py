from django.contrib import admin
from .models import Category,Post, SubCategory
from django import forms
from ckeditor.widgets import CKEditorWidget


admin.site.register(SubCategory)
class PostAdminForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        fields = '__all__'
        model = Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')
    list_display=('title','author','published','post_categories','post_subcategories')
    ordering=('published',)
    search_fields=('title','author__username','content')
    date_hierarchy=('published')
    list_filter=('author__username','categories__name')
    form = PostAdminForm

    def post_categories(self,obj):
        return ' ,'.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description= 'categorías'

    def post_subcategories(self,obj):
        return ' ,'.join([c.name for c in obj.subcategories.all().order_by('name')])
    post_subcategories.short_description= 'Subcategorías'


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)








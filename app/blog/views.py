from django.shortcuts import render, get_object_or_404
from .models import Post,Category, SubCategory
from django.views.generic import DetailView
from django.views.generic import ListView

# Create your views here.

class blog(ListView):
    model = Post
    template_name = "blog/blog.html"
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all
        context['categories'] = categories
        return context

def category(request, category_id):
    category = get_object_or_404(Category, id= category_id)
    categories = Category.objects.all
    return render(request,"blog/category.html",{'category': category,'categories':categories})



def subcategory(request, subcategory_id):
    subcategory = get_object_or_404 (SubCategory, id= subcategory_id)
    categories = Category.objects.all
    return render(request,"blog/subcategory.html",{'subcategory': subcategory,'categories':categories})



class BlogDetailView(DetailView):

    model = Post
    template_name = 'blog/entrada.html'

def buscadorblog(request,*args,**kwargs):
    busqueda= request.POST.get('buscador')
    post= Post.objects.filter(title__icontains=busqueda)|Post.objects.filter(content__icontains=busqueda)
    return render (request,"blog/buscarblog.html",{'post':post})
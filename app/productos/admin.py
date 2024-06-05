from django.contrib import admin
from .models import Producto, Dosisproducto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','media2',)
    def save_model(self, request, obj, form, change):
        if not obj.pk: # call super method if object has no primary key
            super(ProductoAdmin, self).save_model(request, obj, form, change)
        else:
            pass # don't actually save the parent instance

    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)
        super(ProductoAdmin, self).save_model(request, form.instance, form, change)

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Dosisproducto)
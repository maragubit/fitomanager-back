from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('plantas', 'indicaciones')
        widgets = {

            'plantas': forms.Select,
            'indicaciones':forms.Select,
        }


    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['plantas'].empty_label = "Todas"
        self.fields['indicaciones'].label = "Etiquetas"
        self.fields['indicaciones'].empty_label = "Todas"
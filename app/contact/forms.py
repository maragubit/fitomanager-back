from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV2Invisible, ReCaptchaV3

class Formulario(forms.Form):
    nombre= forms.CharField(label='Nombre',required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField(label='Email',required=True,widget= forms.EmailInput(attrs={'class':'form-control'}))
    contenido=forms.CharField(label='Consulta',required=True, widget= forms.Textarea(attrs={'class':'form-control','rows':6}))





class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
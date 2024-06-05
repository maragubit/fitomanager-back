from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Formulario, FormWithCaptcha
from django.core.mail import EmailMessage

# Create your views here.
def contact (request):
    contactform = Formulario()
    captchaform = FormWithCaptcha
    if request.method == 'POST':
        contactform = Formulario(data=request.POST)
        if contactform.is_valid():
            nombre= request.POST.get('nombre')
            email= request.POST.get('email')
            contenido= request.POST.get('contenido')
            #enviamos email:
            # Creamos el correo
            emailprueba = EmailMessage(
                "Fitomanager: Nueva consulta recibida",
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, email, contenido),
                "no-contestar@inbox.mailtrap.io",
                ["fitomanager@gmail.com"],

            )

            # Lo enviamos y redireccionamos
            try:
                emailprueba.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
            return redirect(reverse('contact')+'?ok')
    return render (request,"contact/contact.html", {'formulario':contactform, 'captchaform':captchaform})
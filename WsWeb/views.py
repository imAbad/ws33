from email import message
from re import sub, template
from urllib import request
from django.shortcuts import render, redirect
from Apps.Propiedades.models import Properties
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from django.template.loader import get_template, render_to_string
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def acapulcoGolden(request):
    return render(request, "acapulcoGolden.html")


def agents(request):
    return render(request, "agents-grid.html")


def contact(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = 'Nombre: ' + request.POST.get('name') + '\nCorreo: ' + request.POST.get('email') + '\nMensaje: ' + request.POST.get('message')
        email = settings.EMAIL_HOST_USER
        
        recipient_list = ['contact@giwsrealestate33.com.mx']
        
        send_mail(subject, message, email, recipient_list)
        return render(request, 'contact.html')
        
    return render(request, 'contact.html')


        







def services(request):
    return render(request, "services.html")


def Property(request):
    property = Properties.objects.all()

    return render(request, "property-single.html", {'property': property})


def busquedaPropiedades(request):
    #queryset = request.GET.get("palabra")
    """
    property = propiedades.objects.filter(estado=True)

    if queryset:
        property = propiedades.object.filter(

            Q(nombrePropiedad=queryset) |
            Q(tipoPropiedad=queryset) |
            Q(tipOperacion=queryset) |
            Q(tipoAmenidades=queryset) |
            Q(ubicacion=queryset) |
            Q(costo=queryset)


      ).distinct()
      #Añadir este diccionario al final del return en caso de ser necesario
      {'property': property}
     """

    return render(request, "property-grid.html")

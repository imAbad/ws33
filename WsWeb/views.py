from email import message
from re import sub, template
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from Apps.Propiedades.models import Properties, imagenPropiedades
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from django.template.loader import get_template, render_to_string
from django.contrib import messages
from django.views.generic.detail import DetailView


def index(request):
    propiedades = Properties.objects.all()
    context = {
        'propiedades': propiedades
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def acapulcoGolden(request):
    return render(request, "acapulcoGolden.html")


def agents(request):
    return render(request, "agents-grid.html")


def contact(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = 'Nombre: ' + request.POST.get('name') + '\nCorreo: ' + request.POST.get(
            'email') + '\nMensaje: ' + request.POST.get('message')
        email = settings.EMAIL_HOST_USER

        recipient_list = ['contact@giwsrealestate33.com.mx']

        send_mail(subject, message, email, recipient_list)
        return render(request, 'contact.html')

    return render(request, 'contact.html')


def services(request):
    return render(request, "services.html")


def Property(request, pk):
    propiedad = get_object_or_404(Properties, pk = pk)
    img = imagenPropiedades.objects.filter(propiedad = propiedad)
    context = {'propiedad': propiedad,
               'img' : img
               }

    return render(request, "property-single.html", context)





def busquedaPropiedades(request):
    propiedades = Properties.objects.all()
    context = {
        'propiedades': propiedades
    }
    return render(request, "property-grid.html", context)

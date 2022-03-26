from django.shortcuts import render
from Apps.Propiedades.models import Properties


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def acapulcoGolden(request):
    return render(request, "acapulcoGolden.html")


def agents(request):
    return render(request, "agents-grid.html")


def contact(request):
    return render(request, "contact.html")


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

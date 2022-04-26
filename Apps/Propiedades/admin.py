from django.contrib import admin
from .models import Properties, imagenPropiedades

# Register your models here.

class ImagePropiedadesAdmin(admin.TabularInline):
    model = imagenPropiedades

class PropiedadesAdmin(admin.ModelAdmin):
    
    inlines = [
        ImagePropiedadesAdmin
    ]

admin.site.register(Properties, PropiedadesAdmin)


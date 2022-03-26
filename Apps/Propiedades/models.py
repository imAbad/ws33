from django.db import models
import uuid

# Create your models here.


class Properties(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombrePropiedad = models.CharField(max_length=40, null=True)

    def __str__(self):
        return"{0}".format(self.nombrePropiedad)
    tipos = [
        ('Cas', 'Casa'),
        ('Dep', 'Departamento'),
        ('Vil', 'Villa'),
        ('Res', 'Residencia'),
        ('Ofi', 'Oficina'),
        ('Ter', 'Terreno'),
        ('Bod', 'Bodega'),
        ('Des', 'Desarrollo'),
        ('Edi', 'Edificio')
    ]
    tipoPropiedad = models.CharField(
        max_length=12, choices=tipos, default='Casa')
    operaciones = [
        ('Venta', 'Venta'),
        ('Renta', 'Renta')
    ]
    tipOperacion = models.CharField(
        max_length=5, choices=operaciones, default='V')
    amenidades = [
        ('AC', 'Aire Acondicionado'), ('CCTV', 'Camaras de Seguridad'), ('Security', 'Seguridad privada'), ('Tenis', 'Cancha de tenis'), ('Futbol', 'Cancha de fútbol'), ('Terraza', 'Terraza'), ('Alberca', 'Alberca'), ('Jacuzzi', 'Jacuzzi'), ('internet', 'WiFi'), ('Cocina', 'Cocina Integral'), ('Aljibe', 'Aljibe'), ('Vista', 'Vista al Mar'), ('GYM', 'Gimnasio'), ('AreasVerdes', 'Áreas Verdes')
    ]
    tipoAmenidades = models.TextField(max_length=25, choices=amenidades)
    descripcion = models.TextField(max_length=2000, null=False, blank=False)
    ubicacion = models.CharField(max_length=35, null=False, blank=False)
    costo = models.SlugField(max_length=255, null=False)
    habitaciones = models.IntegerField(default=0, null=False, blank=False)
    banos = models.IntegerField(default=0, null=False, blank=False)
    estacionamientos = models.IntegerField(default=0, null=False, blank=False)
    metrosTerreno = models.IntegerField(default=0, null=False, blank=False)
    metrosConstruccion = models.IntegerField(
        default=0, null=False, blank=False)
    pisos = models.IntegerField(blank=True)

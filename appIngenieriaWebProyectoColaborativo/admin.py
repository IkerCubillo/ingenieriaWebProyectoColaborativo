from django.contrib import admin
from .models import Pelicula, Personaje, Raza, SubRaza

admin.site.register(Pelicula)
admin.site.register(Personaje)
admin.site.register(Raza)
admin.site.register(SubRaza)
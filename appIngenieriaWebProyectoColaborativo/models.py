from django.db import models
 
class Raza(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
 
class Personaje(models.Model):
    # Campo para la relación one-to-many (un personaje pertenece a una raza)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (un personaje participa en varias peliculas)
    pelicula = models.ManyToManyField(Pelicula)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    antiguedad = models.IntegerField(default=0)
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.       	

    def __str__(self):
        return self.nombre
from django.db import models
 
class Raza(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)


    def __str__(self):
        return self.nombre
    
class SubRaza(models.Model):
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)

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
    subRaza = models.ForeignKey(SubRaza, on_delete=models.CASCADE, null=True, blank=True)

    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=50)
    estatura = models.FloatField(default=1.80)

    edadTierra = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_muerte = models.DateField(null=True, blank=True)

    # Campo para la relación many-to-many (un personaje participa en varias peliculas)
    peliculas = models.ManyToManyField(Pelicula)     	

    def __str__(self):
        return self.nombre
    

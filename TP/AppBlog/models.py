from django.db import models

# Create your models here.
class Pelicula(models.Model):

    titulo = models.CharField(max_length=50)
    fecha_Estreno= models.DateField()
    genero=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    productora=models.CharField(max_length=50)
    calificacion=models.IntegerField()

class Director(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    nacionalidad=models.CharField(max_length=50)
    
class Productora(models.Model):

    nombre = models.CharField(max_length=50)
    inicio_act=models.DateField()
    pais=models.CharField(max_length=50)




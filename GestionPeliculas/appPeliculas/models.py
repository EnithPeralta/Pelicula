from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    
    def __str__(self)->str:
        return self.nombre

class Pelicula(models.Model):
    codigo = models.CharField(max_length=9)
    titulo = models.CharField(max_length=50)
    protagonista = models.CharField(max_length=50)
    duracion = models.IntegerField()
    resumen = models.CharField(max_length=2000)
    foto = models.ImageField(upload_to=f"fotos/",null=True, blank=True)
    genero = models.ForeignKey(Genero,on_delete=models.PROTECT)
    
    def __str__(self)->str:
        return self.titulo
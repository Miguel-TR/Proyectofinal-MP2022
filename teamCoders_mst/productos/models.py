from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to="productos", null=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Fruto'
        verbose_name_plural='Frutos'
        ordering=["-created"]

    def __str__(self):
        return self.nombre

opciones_consulta = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)   
    correo = models.EmailField()
    tipoConsulta = models.IntegerField(choices = opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField

    def __str__(self):
        return self.nombre


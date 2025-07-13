from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    url = models.URLField(blank=True)
    archivo_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)  # ← NUEVO CAMPO

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='calificaciones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.libro.nombre} ({self.puntuacion})"

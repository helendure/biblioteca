from django.contrib import admin
from .models import Autor, Genero, Libro, Calificacion

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Calificacion)

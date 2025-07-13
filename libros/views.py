from django.shortcuts import render, redirect
from .models import Libro, Calificacion
from .forms import LibroForm
from django.contrib.auth.decorators import login_required

# Página principal
def home(request):
    return render(request, 'libros/home.html')


# Subir libro
@login_required
def subir_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/subir_libro.html', {'form': form})


# Función para obtener libros similares
def obtener_libros_similares(libro):
    return Libro.objects.filter(
        genero=libro.genero
    ).exclude(id=libro.id)[:3]


# Listar libros + similares
def listar_libros(request):
    libros = Libro.objects.all()
    libros_con_similares = []
    for libro in libros:
        similares = obtener_libros_similares(libro)
        libros_con_similares.append((libro, similares))
    return render(request, 'libros/listar_libros.html', {'libros_con_similares': libros_con_similares})


# Calificar libro
@login_required
def calificar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    if request.method == 'POST':
        puntuacion = int(request.POST.get('puntuacion'))
        comentario = request.POST.get('comentario', '')
        Calificacion.objects.create(
            libro=libro,
            usuario=request.user,
            puntuacion=puntuacion,
            comentario=comentario
        )
        return redirect('listar_libros')
    return render(request, 'libros/calificar_libro.html', {'libro': libro})

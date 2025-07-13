from django.urls import path
from . import views

urlpatterns = [
    path('subir/', views.subir_libro, name='subir_libro'),
    path('listar/', views.listar_libros, name='listar_libros'),
    path('calificar/<int:libro_id>/', views.calificar_libro, name='calificar_libro'),
]

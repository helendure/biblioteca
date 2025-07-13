from django.urls import path
from . import api_views

urlpatterns = [
    path('autor/', api_views.autor_listar, name='autor_listar'),
    path('autor/nuevo/', api_views.autor_nuevo, name='autor_nuevo'),
    path('autor/<int:pk>/', api_views.autor_detalle, name='autor_detalle'),
    path('autor/<int:pk>/editar/', api_views.autor_actualizar, name='autor_actualizar'),
    path('autor/<int:pk>/eliminar/', api_views.autor_eliminar, name='autor_eliminar'),

    path('genero/', api_views.genero_listar, name='genero_listar'),
    path('genero/nuevo/', api_views.genero_nuevo, name='genero_nuevo'),
    path('genero/<int:pk>/', api_views.genero_detalle, name='genero_detalle'),
    path('genero/<int:pk>/editar/', api_views.genero_actualizar, name='genero_actualizar'),
    path('genero/<int:pk>/eliminar/', api_views.genero_eliminar, name='genero_eliminar'),

    path('libro/', api_views.libro_listar, name='libro_listar'),
    path('libro/nuevo/', api_views.libro_nuevo, name='libro_nuevo'),
    path('libro/<int:pk>/', api_views.libro_detalle, name='libro_detalle'),
    path('libro/<int:pk>/editar/', api_views.libro_actualizar, name='libro_actualizar'),
    path('libro/<int:pk>/eliminar/', api_views.libro_eliminar, name='libro_eliminar'),

    path('calificacion/', api_views.calificacion_listar, name='calificacion_listar'),
    path('calificacion/nueva/', api_views.calificacion_nueva, name='calificacion_nueva'),
    path('calificacion/<int:pk>/', api_views.calificacion_detalle, name='calificacion_detalle'),
    path('calificacion/<int:pk>/editar/', api_views.calificacion_actualizar, name='calificacion_actualizar'),
    path('calificacion/<int:pk>/eliminar/', api_views.calificacion_eliminar, name='calificacion_eliminar'),

]

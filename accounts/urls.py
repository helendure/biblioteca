from django.urls import path
from .views import login_view, cerrar_sesion

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]

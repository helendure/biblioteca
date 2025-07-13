from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'autor', 'genero', 'fecha_lanzamiento', 'url', 'archivo_pdf']  
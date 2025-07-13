from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from libros.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('libros.api_urls')),
    path('libros/', include('libros.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

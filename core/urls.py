"""
URL configuration for core project.

"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  #  Importa as configurações 
from django.conf.urls.static import static  #  Importa os arquivos da pasta static que esta na BASE-DIR do projeto

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pacientes/', include('pacientes.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

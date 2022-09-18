from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("mensajeFormulario/",mensajeFormulario,name="mensajeFormulario"),
    path("leerMensaje/",leerMensaje,name="leerMensaje"),
    path("misMensajes/<id>",misMensajes,name="misMensajes"),
    path("eliminarMensajes/<id>",eliminarMensajes,name="eliminarMensajes"),
]
from sqlite3 import Cursor
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns=[
    
    path("",concesionario, name="inicio"),
    path("clienteFormulario/",clienteFormulario,name="clienteFormulario"),
    path("autoFormulario/",autoFormulario,name="autoFormulario"),
    path("postFormulario/",postFormulario,name="postFormulario"),
    path("busquedaPost/",busquedaPost,name="busquedaPost"),
    path("busquedaCliente/",busquedaCliente,name="busquedaCliente"),
    path("busquedaAuto/",busquedaAuto,name="busquedaAuto"),
    path("buscar_post/",buscar_post,name="buscar_post"),
    path("buscar_auto/",buscar_auto,name="buscar_auto"),
    path("buscar_cliente/",buscar_cliente,name="buscar_cliente"),
    path("leerAutos/", leerAutos, name="leerAutos"),
    path("leerClientes/", leerClientes, name="leerClientes"),
    path("leerPosts/", leerPosts, name="leerPosts"),
    path("eliminarAuto/<id>", eliminarAuto, name="eliminarAuto"),
    path("eliminarCliente/<id>", eliminarCliente, name="eliminarCliente"),
    path("eliminarPost/<id>", eliminarPost, name="eliminarPost"),
    path("login/",login_request,name="login"),
    path("register/",register,name="register"),
    path("logout/",LogoutView.as_view(template_name="concesionario/logout.html"),name="logout"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
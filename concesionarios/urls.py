from sqlite3 import Cursor
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns=[
    
    path("",concesionario, name="inicio"),
    path("clienteFormulario/",clienteFormulario,name="clienteFormulario"),
    path("autoFormulario/",autoFormulario,name="autoFormulario"),
    path("sucursalFormulario/",sucursalFormulario,name="sucursalFormulario"),
    path("busquedaSucursal/",busquedaSucursal,name="busquedaSucursal"),
    path("busquedaCliente/",busquedaCliente,name="busquedaCliente"),
    path("busquedaAuto/",busquedaAuto,name="busquedaAuto"),
    path("buscar_sucursal/",buscar_sucursal,name="buscar_sucursal"),
    path("buscar_auto/",buscar_auto,name="buscar_auto"),
    path("buscar_cliente/",buscar_cliente,name="buscar_cliente"),
    path("leerAutos/", leerAutos, name="leerAutos"),
    path("leerClientes/", leerClientes, name="leerClientes"),
    path("leerSucursales/", leerSucursales, name="leerSucursales"),
    path("eliminarAuto/<id>", eliminarAuto, name="eliminarAuto"),
    path("eliminarCliente/<id>", eliminarCliente, name="eliminarCliente"),
    path("eliminarSucursal/<id>", eliminarSucursal, name="eliminarSucursal"),
    path("login/",login_request,name="login"),
    path("register/",register,name="register"),
    path("logout/",LogoutView.as_view(template_name="concesionario/logout.html"),name="logout"),
]
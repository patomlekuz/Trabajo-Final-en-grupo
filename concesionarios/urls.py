from sqlite3 import Cursor
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns=[
    
    path("",concesionario, name="inicio"),
    
    path("postFormulario/",postFormulario,name="postFormulario"),
    path("busquedaPost/",busquedaPost,name="busquedaPost"),
    path("busquedaCliente/",busquedaCliente,name="busquedaCliente"),
    path("busquedaAuto/",busquedaAuto,name="busquedaAuto"),
    path("buscar_post/",buscar_post,name="buscar_post"),
    path("aboutus/",aboutus,name="aboutus"),
    path("leerPosts/", leerPosts, name="leerPosts"),
    path("eliminarPost/<id>", eliminarPost, name="eliminarPost"),
    path("login/",login_request,name="login"),
    path("register/",register,name="register"),
    path("logout/",LogoutView.as_view(template_name="concesionario/logout.html"),name="logout"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
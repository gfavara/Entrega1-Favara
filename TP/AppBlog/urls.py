from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("pelis/", pelis, name="pelis"),
    path("dires/", dires, name="dires"),
    path("produ/", produ, name="produ"),
    path("productoras/buscar/resultados/", resultados_busqueda_productoras, name="productora_resul"),
    path("directores/buscar/resultados/", resultados_busqueda_dires, name="director_resul"),
    path("peliculas/buscar/resultados/", resultados_busqueda_pelis, name="peli_resul"),
    path("login/", iniciar_sesion, name="auth-login"),
    path("registro/", registrar_usuario, name="auth-register"),
    path("logout/", cerrar_sesion, name="auth-logout"),
    path("perfil/editar/", editar_perfil, name="auth-editar-perfil"),
    path("perfil/avatar/", agregar_avatar, name="auth-avatar"),
    path('delete_item_dir/<int:id>', delete_item_director, name="delete_item_dir"),
]
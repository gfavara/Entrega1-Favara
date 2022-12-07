from django.urls import path
from AppBlog.views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path("directores/borrar/<pk>", directorDelete.as_view(), name="director-delete"),
    path("directores/actualizar/<pk>", directorEdit.as_view(), name="director-edit"),
    path("directores/listar/", directorList.as_view(), name="director-list"),
    path("directores/detalle/<pk>", directorDetail.as_view(), name="director-detail"),
    path("peliculas/borrar/<pk>", peliculaDelete.as_view(), name="pelicula-delete"),
    path("peliculas/actualizar/<pk>", peliculaEdit.as_view(), name="pelicula-edit"),
    path("peliculas/listar/", peliculaList.as_view(), name="pelicula-list"),
    path("peliculas/detalle/<pk>", peliculaDetail.as_view(), name="pelicula-detail"),
    path("productoras/borrar/<pk>", productoraDelete.as_view(), name="productora-delete"),
    path("productoras/actualizar/<pk>", productoraEdit.as_view(), name="productora-edit"),
    path("productoras/listar/", productoraList.as_view(), name="productora-list"),
    path("productoras/detalle/<pk>", productoraDetail.as_view(), name="productora-detail"),
    path("about", about, name="about"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
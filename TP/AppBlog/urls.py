from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("pelis/", pelis, name="pelis"),
    path("dires/", dires, name="dires"),
    path("produ/", produ, name="produ"),
    path("productoras/buscar/resultados/", resultados_busqueda_productoras, name="productora_resul"),
    path("directores/buscar/resultados/", resultados_busqueda_dires, name="director_resul"),
    
]
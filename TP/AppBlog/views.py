from django.shortcuts import render
from django.http import HttpRequest
import datetime
from AppBlog.forms import *
from AppBlog.models import *

def homepage(request):
    

    return render(request, 'homepage.html')

def pelis(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
 
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            pelicula = Pelicula(titulo=data["titulo"],fecha_Estreno=data["fecha_Estreno"], genero=data["genero"], director=data["director"], productora=data["productora"], calificacion=data["calificacion"])

            pelicula.save()
    formulario = PeliculaForm()    
    contexto = {"formulario": formulario}
    return render(request, "peliculas.html",contexto)




def resultados_busqueda_pelis(request):
    titulo = request.GET["nombre_peli"]

    peliculas = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(request, "resultado_pelis.html", {"peliculas":peliculas})




def dires(request):
    if request.method == "POST":
        formulario = DirectorForm(request.POST)
 
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            director = Director(nombre=data["nombre"],apellido=data["apellido"], fecha_nac=data["fecha_nac"], nacionalidad=data["nacionalidad"])

            director.save()
    formulario = DirectorForm()    
    contexto = {"formulario": formulario}
    return render(request, "directores.html",contexto)   

def resultados_busqueda_dires(request):
    nombre = request.GET["nombre_director"]

    directores = Director.objects.filter(nombre__icontains=nombre)
    return render(request, "resultado_dires.html", {"directores":directores})

    
def produ(request):
    if request.method == "POST":
        formulario = ProductoraForm(request.POST)
 
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            productora = Productora(nombre=data["nombre"], inicio_act=data["inicio_act"], pais=data["pais"])

            productora.save()
    formulario = ProductoraForm()    
    contexto = {"formulario": formulario}
    return render(request, "productoras.html",contexto)   




def resultados_busqueda_productoras(request):
    nombre = request.GET["nombre_productora"]

    productoras = Productora.objects.filter(nombre__icontains=nombre)
    return render(request, "resultado_productora.html", {"productoras":productoras})
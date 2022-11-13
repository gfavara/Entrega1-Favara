from django.shortcuts import render
from django.http import HttpRequest
import datetime
from AppBlog.forms import *
from AppBlog.models import *

def homepage(request):
    

    return render(request, 'homepage.html')

def pelis(request):
    

    return render(request, 'peliculas.html')    

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
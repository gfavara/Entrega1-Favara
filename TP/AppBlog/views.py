import datetime

from AppBlog.forms import *
from AppBlog.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView,  UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def homepage(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, 'homepage.html', {"imagen_url":imagen_url})

@login_required
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



@login_required
def resultados_busqueda_pelis(request):
    titulo = request.GET["nombre_peli"]

    peliculas = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(request, "resultado_pelis.html", {"peliculas":peliculas})

@login_required
def delete_item_director(request,id):
    Director.objects.get(id=id).delete()
   
    # idd=request.GET["delete_item_dir"]
    # Director.objects.get(id=idd).delete()    
    directores = Director.objects.all()
    
    return render(request,"resultado_dires.html", {"directores":directores})




@login_required
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

@login_required
def resultados_busqueda_dires(request):
    nombre = request.GET["nombre_director"]

    directores = Director.objects.filter(nombre__icontains=nombre)
    return render(request, "resultado_dires.html", {"directores":directores})

@login_required    
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


@login_required
def resultados_busqueda_productoras(request):
    nombre = request.GET["nombre_productora"]

    productoras = Productora.objects.filter(nombre__icontains=nombre)
    return render(request, "resultado_productora.html", {"productoras":productoras})

    

def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                return render(request, "login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "login.html", {"form": formulario, "errors": errors})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("homepage")

def registrar_usuario(request):
     
    if request.method =="POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("homepage")
        else:
            return render(request, "register.html", { "formulario": formulario, "errors": formulario.errors})

    formulario  = UserRegisterForm()
    return render(request, "register.html", { "formulario": formulario})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        # * cargar informacion en el formulario
        formulario = UserEditForm(request.POST)

        # ! validacion del formulario
        if formulario.is_valid():
            data = formulario.cleaned_data

            # * actualizacion del usuario con los datos del formulario
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("homepage")
        else:
            return render(request, "editar_perfil.html", {"form": formulario, "errors": formulario.errors})
    else:
        # * crear formulario vacio
        formulario = UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})

    return render(request, "editar_perfil.html", {"form": formulario})


@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        formulario = AvatarForm(request.POST, files=request.FILES)
        print(request.FILES, request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("homepage")
        else:
            return render(request, "agregar_avatar.html", {"form": formulario, "errors": formulario.errors })
    formulario = AvatarForm()

    return render(request, "agregar_avatar.html", {"form":formulario})




class directorDelete(DeleteView):

    model = Director
    success_url = "/dires/"

class directorEdit(UpdateView):

    model = Director
    success_url = "/dires/"
    fields = ["fecha_nac", "nacionalidad"]

class directorList(LoginRequiredMixin, ListView):

    model = Director
    template_name = "list_director.html"


class directorDetail(DetailView):

    model = Director
    template_name = "detail_director.html"





class peliculaDelete(DeleteView):

    model = Pelicula
    success_url = "/pelis/"

class peliculaEdit(UpdateView):

    model = Pelicula
    success_url = "/pelis/"
    fields = ["titulo", "director"]

class peliculaList(LoginRequiredMixin, ListView):

    model = Pelicula
    template_name = "pelicula_list.html"


class peliculaDetail(DetailView):

    model = Pelicula
    template_name = "detail_pelicula.html"
from django import forms

class ProductoraForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    inicio_act=forms.DateField()
    pais=forms.CharField(max_length=50)


class PeliculaForm(forms.Form):

    titulo = forms.CharField(max_length=50)
    fecha_Estreno= forms.DateField()
    genero=forms.CharField(max_length=50)
    director=forms.CharField(max_length=50)
    productora=forms.CharField(max_length=50)
    calificacion=forms.IntegerField()

class DirectorForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_nac = forms.DateField()
    nacionalidad=forms.CharField(max_length=50)
    
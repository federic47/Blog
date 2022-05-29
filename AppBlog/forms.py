from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class NewsFormulario(forms.Form):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    imagen= models.ImageField(upload_to='posteo', blank=True, null=True)

class SportsFormulario(forms.Form):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    imagen= models.ImageField(upload_to='posteo', blank=True, null=True)


class EconomyFormulario(forms.Form):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    imagen= models.ImageField(upload_to='posteo', blank=True, null=True)

class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')
        help_texts={campito:"" for campito in fields}


class UserEditForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    last_name= forms.CharField(label="Modificar Apellido")
    first_name= forms.CharField(label="Modificar Nombre")


    class Meta:
        model=User
        fields=('email', 'password1', 'password2', 'last_name', 'first_name')
        help_texts={campito:"" for campito in fields}

class AvatarForm(forms.Form):
    avatar= forms.ImageField(label="Avatar")

class MensajeForm(forms.Form):
    usuario= forms.CharField(max_length=50)
    asunto = forms.CharField(max_length=50)
    campo= forms.CharField(max_length=250)
    


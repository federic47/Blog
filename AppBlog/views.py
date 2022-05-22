from django.http import HttpResponse
from django .views.generic import ListView
from django .views.generic.detail import DetailView
from django .views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from AppBlog.forms import NewsFormulario,UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



#--------Definimos la views de inicio------------------#
def inicio(request):
    return render(request,'AppBlog/inicio.html')

#---------Definimos la views de About---------------------#
def about(request):
    return render(request,'AppBlog/about.html')

#----------Definimos la views de Login---------------------#
def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')
            user=authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)
                return render(request, 'AppBlog/inicio.html', {'usuario':usuario, 'mensaje':'Bienvenido al sistema'})
            else:
                return render(request, 'AppBlog/login.html', {'formulario':formulario, 'mensaje':'USUARIO INCORRECTO, VUELVA A LOGUEAR'})
        else:
            return render(request, 'AppBlog/login.html', {'formulario':formulario, 'mensaje':'FORMULARIO INVALIDO, VUELVA A LOGUEAR'})
    
    else:
        formulario=AuthenticationForm()
        return render(request, 'AppBlog/login.html', {'formulario':formulario})

#------------------------------Definimos la views de register--------------------------#
def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'AppBlog/inicio.html', {'mensaje':f'USUARIO: {username} CREADO EXITOSAMENTE'})
        
    else:
        formulario = UserRegistrationForm()
        return render(request, 'AppBlog/register.html', {'formulario':formulario})


#----------------------------Defino la views de Logout ------------------------------------------------------ 35



#-----------Defino la vista de formulario -----------------#
def newsFormulario(request):

    if request.method == 'POST':
          miFormulario = NewsFormulario(request.POST)
          print(miFormulario)
          
          if miFormulario.is_valid():
              informacion = miFormulario.changed_data
              new = Culture(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'], autor=informacion['autor'], fecha=informacion['fecha'])
              new.save()
              return render(request,'AppBlog/inicio.html')
    else:
        miFormulario= NewsFormulario()
    return render(request,'AppBlog/newsFormulario.html', {'miFormulario': miFormulario})

#*******************************************************************************
def busquedaNews(request):
    return render(request, 'AppBlog/BusquedaNews.html') 


def buscar(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        news = Culture.objects.filter(titulo=titulo)
        return render (request,'AppBlog/resultadosBusqueda.html', {'news': news, 'titulo':titulo})
    else:
        repuesta = "No se ingreso ningun titulo"
        return HttpResponse(repuesta)

    

          
        
       
    











#*************************Clases basadas en Vistas********************#

#--------------------------Clase Culture------------------------------#
class CultureList(ListView):
    model = Culture
    template_name = 'AppBlog/culture_list.html'

class CultureDetalle(DetailView):
    model = Culture
    template_name = 'AppBlog/culture_detalle.html'

class CultureCreacion(CreateView):
    model = Culture
    success_url= reverse_lazy('culture_listar')
    fields= ['titulo','subtitulo','cuerpo','autor','fecha']

class CultureEdicion(UpdateView):
    model = Culture
    success_url= reverse_lazy('culture_listar')
    fields= ['titulo','subtitulo','cuerpo','autor','fecha']

class CultureEliminacion(DeleteView):
    model = Culture
    success_url= reverse_lazy('culture_listar')
    fields= ['titulo','subtitulo','cuerpo','autor','fecha']

#--------------------------Clase Sport------------------------------#

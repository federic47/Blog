from django.http import HttpResponse
from django .views.generic import ListView
from django .views.generic.detail import DetailView
from django .views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from AppBlog.forms import NewsFormulario



#--------Definimos la views de inicio------------------#
def inicio(request):
    return render(request,'AppBlog/inicio.html')


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

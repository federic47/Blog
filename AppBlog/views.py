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
              new = News(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'], autor=informacion['autor'], fecha=informacion['fecha'])
              new.save()
              return render(request,'AppBlog/inicio.html')
    else:
        miFormulario= NewsFormulario()
    return render(request,'AppBlog/newsFormulario.html', {'miFormulario': miFormulario})

     
          
        
       
    











#*************************Clases basadas en Vistas********************#
class NewsList(ListView):
    model = News
    template_name = 'AppBlog/news_list.html'

class NewsDetalle(DetailView):
    model = News
    template_name = 'AppBlog/news_detalle.html'

class NewsCreacion(CreateView):
    model = News
    success_url= reverse_lazy('new_listar')
    fields= ['titulo','subtitulo','cuerpo','autor','fecha']

class NewsEdicion(UpdateView):
    model = News
    success_url= reverse_lazy('new_listar')
    fields= ['titulo','subtitulo','cuerpo','autor','fecha']

class NewsEliminacion(DeleteView):
    model = News
    success_url= reverse_lazy('new_listar')
    fields= ['titulo','subtitulo','cuerpo','autor','fecha']

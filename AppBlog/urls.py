from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio, name='inicio'),



    path('newsFormulario/', newsFormulario, name='newsFormulario'),
    path('busquedaNews/', busquedaNews, name='busquedaNews'),
    path('buscar/', buscar, name='buscar'),

    path('about/', about , name='about'),
    path('login', login_request, name='login'),
    path('register',register, name='register'),
    path('logout', LogoutView.as_view(template_name="AppBlog/logout.html"), name='logout'),
    path('editarPerfil', editarPerfil, name='editarPerfil'),

    path('culture/list/',CultureList.as_view(),name ='culture_listar' ),
    path('new/<pk>', CultureDetalle.as_view(), name='culture_detalle'),
    path('new/nuevo/', CultureCreacion.as_view(), name='culture_crear'),
    path('new/editar/<pk>',CultureEdicion.as_view(), name='culture_editar'),
    path('new/borrar/<pk>',CultureEliminacion.as_view(), name='culture_borrar'),

]
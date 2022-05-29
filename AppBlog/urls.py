from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio, name='inicio'),
    

    path('about/', about , name='about'),
    path('login', login_request, name='login'),
    path('register',register, name='register'),
    path('logout', LogoutView.as_view(template_name="AppBlog/logout.html"), name='logout'),
    path('editarPerfil', editarPerfil, name='editarPerfil'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),
    path('enviarMensaje', enviarMensaje, name='enviarMensaje'),
    path('buscarMensaje', buscarMensajes, name='buscarMensajes'),

    path('culture/list/',CultureList.as_view(),name ='culture_listar' ),
    path('new/<pk>', CultureDetalle.as_view(), name='culture_detalle'),
    path('new/nuevo/', CultureCreacion.as_view(), name='culture_crear'),
    path('new/editar/<pk>',CultureEdicion.as_view(), name='culture_editar'),
    path('new/borrar/<pk>',CultureEliminacion.as_view(), name='culture_borrar'),

    path('sports/list/',SportList.as_view(),name ='sports_listar' ),
    path('sports/<pk>', SportsDetalle.as_view(), name='sports_detalle'),
    path('sports/nuevo/', SportCreacion.as_view(), name='sports_crear'),
    path('sports/editar/<pk>',SportsEdicion.as_view(), name='sports_editar'),
    path('sports/borrar/<pk>',SportsEliminacion.as_view(), name='sports_borrar'),

    path('economy/list/',EconomyList.as_view(),name ='economy_listar' ),
    path('eco/<pk>', EconomyDetalle.as_view(), name='economy_detalle'),
    path('eco/nuevo/', EconomyCreacion.as_view(), name='economy_crear'),
    path('eco/editar/<pk>',EconomyEdicion.as_view(), name='economy_editar'),
    path('eco/borrar/<pk>',EconomyEliminacion.as_view(), name='economy_borrar'),

]
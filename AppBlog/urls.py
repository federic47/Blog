from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),



    path('newsFormulario/', newsFormulario, name='newsFormulario'),
    path('busquedaNews/', busquedaNews, name='busquedaNews'),
    path('buscar/', buscar, name='buscar'),

    path('new/list/',NewsList.as_view(),name ='new_listar' ),
    path('new/<pk>', NewsDetalle.as_view(), name='new_detalle'),
    path('new/nuevo/', NewsCreacion.as_view(), name='new_crear'),
    path('new/editar/<pk>',NewsEdicion.as_view(), name='new_editar'),
    path('new/borrar/<pk>',NewsEliminacion.as_view(), name='new_borrar'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name='inicio'),



    path('newsFormulario/', newsFormulario, name='newsFormulario'),
    path('busquedaNews/', busquedaNews, name='busquedaNews'),
    path('buscar/', buscar, name='buscar'),

    path('culture/list/',CultureList.as_view(),name ='culture_listar' ),
    path('new/<pk>', CultureDetalle.as_view(), name='culture_detalle'),
    path('new/nuevo/', CultureCreacion.as_view(), name='culture_crear'),
    path('new/editar/<pk>',CultureEdicion.as_view(), name='culture_editar'),
    path('new/borrar/<pk>',CultureEliminacion.as_view(), name='culture_borrar'),

]
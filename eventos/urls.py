from django.urls import path
from .views import ListaEventosView, CrearEventoView, EditarEventoView, EliminarEventoView, nosotros

urlpatterns = [
    path('', ListaEventosView.as_view(), name='lista_eventos'),
    path('crear/', CrearEventoView.as_view(), name='crear_evento'),
    path('editar/<int:pk>/', EditarEventoView.as_view(), name='editar_evento'),
    path('eliminar/<int:pk>/', EliminarEventoView.as_view(), name='eliminar_evento'),
    path('nosotros/', nosotros, name='nosotros'),
]

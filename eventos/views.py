from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evento
from .forms import EventoForm
from django.shortcuts import render

class ListaEventosView(ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'

class CrearEventoView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/crear_evento.html'
    success_url = reverse_lazy('lista_eventos')
    
class EditarEventoView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/editar_evento.html'
    success_url = reverse_lazy('lista_eventos')
    
class EliminarEventoView(DeleteView):
    model = Evento
    template_name = 'eventos/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_eventos')
    
def nosotros(request):
    miembros = [
        {'nombre': 'Juan Pérez', 'detalle': 'Desarrollador Frontend', 'imagen': 'perfil01.jpg'},
        {'nombre': 'Ana López', 'detalle': 'Desarrolladora Backend', 'imagen': 'perfil01.jpg'},
        {'nombre': 'Carlos Ruiz', 'detalle': 'Diseñador UI/UX', 'imagen': 'perfil01.jpg'},
    ]
    return render(request, 'eventos/nosotros.html', {'miembros': miembros})
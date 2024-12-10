from django.views.generic import ListView, DetailView, View
from .models import Raza, Pelicula, Personaje
from django.shortcuts import render

class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Obtener todas las razas
        razas = Raza.objects.all()
        
        # Crear una lista de diccionarios que contiene la raza y su primer personaje
        razas_con_personajes = []
        for raza in razas:
            primer_personaje = Personaje.objects.filter(raza=raza).order_by('nombre').first()
            razas_con_personajes.append({
                'raza': raza,
                'primer_personaje': primer_personaje
            })
        
        # Pasar los datos al contexto
        context = {'razas_con_personajes': razas_con_personajes}
        
        # Renderizar la plantilla con el contexto
        return render(request, 'index.html', context)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Obtener todas las razas
        razas = Raza.objects.all()
        
        # Crear una lista de diccionarios que contiene la raza y su primer personaje
        razas_con_personajes = []
        for raza in razas:
            primer_personaje = Personaje.objects.filter(raza=raza).order_by('nombre').first()
            razas_con_personajes.append({
                'raza': raza,
                'primer_personaje': primer_personaje
            })
        
        # Pasar los datos al contexto
        context = {'razas_con_personajes': razas_con_personajes}
        
        # Renderizar la plantilla con el contexto
        return render(request, 'index.html', context)

# Devuelve el listado personajes
class PersonajeListView(ListView):
    model = Personaje
    template_name = 'index_personajes.html'
    context_object_name = 'lista_personajes'
    queryset = Personaje.objects.order_by('nombre')
    
# Devuelve el listado de razas
class RazaListView(ListView):
    model = Raza
    template_name = 'index_razas.html'
    context_object_name = 'lista_razas'
    queryset = Raza.objects.order_by('nombre')
    
# Devuelve el listado de peliculas
class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'index_peliculas.html'
    context_object_name = 'lista_peliculas'
    queryset = Pelicula.objects.order_by('nombre')

# Devuelve los datos de una raza
class RazaDetailView(DetailView):
    model = Raza
    template_name = 'raza_detail.html'
    context_object_name = 'raza'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        raza = self.get_object()
        context['personajes'] = raza.personaje_set.all()
        return context

# Devuelve los detalles de un personaje
class PersonajeDetailView(DetailView):
    model = Personaje
    template_name = 'personaje_detail.html'
    context_object_name = 'personaje'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personaje = self.get_object()
        context['peliculas'] = personaje.peliculas.all()
        return context

# Devuelve los detalles de una pelicula
class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'pelicula_detail.html'
    context_object_name = 'pelicula'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pelicula = self.get_object()
        context['personajes'] = pelicula.personaje_set.all()
        return context

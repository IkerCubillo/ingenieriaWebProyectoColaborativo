from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Raza, Pelicula, Personaje

# Devuelve el listado personajes
def index_personajes(request):
	personajes = get_list_or_404(Personaje.objects.order_by('nombre'))
	context = {'lista_personajes' : personajes }
	return render(request, 'index_personajes.html', context)

# Devuelve el listado de razas
def index_razas(request):
	razas = get_list_or_404(Raza.objects.order_by('nombre'))
	context = {'lista_razas': razas }
	return render(request, 'index_razas.html', context)

# Devuelve el listado de peliculas
def index_peliculas(request):
	peliculas = get_list_or_404(Pelicula.objects.order_by('nombre'))
	context = {'lista_peliculas': peliculas }
	return render(request, 'index_peliculas.html', context)

def index(request):
    # Obtener todas las razas
    razas = Raza.objects.all()
    
    razas_con_personajes = []
    for raza in razas:
        primer_personaje = Personaje.objects.filter(raza=raza).order_by('nombre').first()
        razas_con_personajes.append({
            'raza': raza,
            'primer_personaje': primer_personaje
        })
    
    return render(request, 'index.html', {'razas_con_personajes': razas_con_personajes})

# Devuelve los datos de una raza
def show_raza(request, raza_id):
	raza = get_object_or_404(Raza, pk=raza_id)
	personajes =  raza.personaje_set.all()
	context = {'personajes': personajes, 'raza': raza }
	return render(request, 'raza_detail.html', context)

# Devuelve los detalles de un personaje
def show_personaje(request, personaje_id):
	personaje = get_object_or_404(Personaje, pk=personaje_id)
	peliculaes =  personaje.peliculas.all()
	context = { 'personaje': personaje, 'peliculas' : peliculaes }
	return render(request, 'personaje_detail.html', context)

# Devuelve los detalles de una pelicula
def show_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    personajes =  pelicula.personaje_set.all()
    context = { 'personajes': personajes, 'pelicula' : pelicula }
    return render(request, 'pelicula_detail.html', context)
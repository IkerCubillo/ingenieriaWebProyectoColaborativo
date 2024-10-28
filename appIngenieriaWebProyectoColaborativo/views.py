from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Raza, Pelicula, Personaje

#devuelve el listado de empresas
def index_razas(request):
	razas = get_list_or_404(Raza.objects.order_by('nombre'))
	context = {'lista_razas': razas }
	return render(request, 'index.html', context)

#devuelve los datos de un raza
def show_raza(request, raza_id):
	raza = get_object_or_404(Raza, pk=raza_id)
	context = {'raza': raza }
	return render(request, 'detail.html', context)

#devuelve los empelados de un raza
def index_personajes(request, raza_id):
	raza = get_object_or_404(Raza, pk=raza_id)
	personajes =  raza.personaje_set.all()
	context = {'raza': raza, 'personajes' : personajes }
	return render(request, 'personajes.html', context)

#devuelve los detalles de un personaje
def show_personaje(request, personaje_id):
	personaje = get_object_or_404(Personaje, pk=personaje_id)
	peliculaes =  personaje.peliculas.all()
	context = { 'personaje': personaje, 'peliculas' : peliculaes }
	return render(request, 'personaje.html', context)

# Devuelve los detalles de una pelicula
def show_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    personajes =  pelicula.personaje_set.all()
    context = { 'personajes': personajes, 'pelicula' : pelicula }
    return render(request, 'pelicula.html', context)
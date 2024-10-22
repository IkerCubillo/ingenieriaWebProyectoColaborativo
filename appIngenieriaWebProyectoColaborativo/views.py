from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Raza, Pelicula, Personaje


#devuelve el listado de razas
def index_razas(request):
	razas = get_list_or_404(Raza.objects.order_by('nombre'))
	output = ', '.join([d.nombre for d in razas])
	return HttpResponse(output)

#devuelve los datos de un raza
def show_raza(request, raza_id):
	raza = get_list_or_404(Raza.objects.get(pk=raza_id))
	output = f'Detalles del raza: {raza.id}, {raza.nombre}, {raza.telefono}'
	return HttpResponse(output)

#devuelve los personajes de un raza
def index_personajes(request, raza_id):
	raza = get_list_or_404(Raza.objects.get(pk=raza_id))
	output = ', '.join([e.nombre for e in raza.personaje_set.all()])
	return HttpResponse(output)

#devuelve los detalles de un personaje
def show_personaje(request, personaje_id):
	personaje = get_list_or_404(Personaje.objects.get(pk=personaje_id))
	output = f'Detalles del personaje: {personaje.id}, {personaje.nombre}, {personaje.fecha_nacimiento}, {personaje.antiguedad}, {str(personaje.raza)}. Peliculas: {[h.nombre for h in personaje.peliculaes.all()]}'
	return HttpResponse(output)

#devuelve los detalles de una pelicula
def show_pelicula(request, pelicula_id):
	pelicula = get_list_or_404(Pelicula.objects.get(pk=pelicula_id))
	output = f'Detalles de la pelicula: {pelicula.id}, {pelicula.nombre}. Personajes: {[e.nombre for e in pelicula.personaje_set.all()]}'
	return HttpResponse(output)
from django.urls import path
from .views import IndexView, PersonajeListView, RazaListView, PeliculaListView, RazaDetailView, PersonajeDetailView, PeliculaDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    path('personajes/', PersonajeListView.as_view(), name='personajes'),
    path('razas/', RazaListView.as_view(), name='razas'),
    path('peliculas/', PeliculaListView.as_view(), name='peliculas'),
    
    path('personajes/<int:pk>/', PersonajeDetailView.as_view(), name='personaje'),
    path('razas/<int:pk>/', RazaDetailView.as_view(), name='raza'),
    path('peliculas/<int:pk>/', PeliculaDetailView.as_view(), name='pelicula'),
]


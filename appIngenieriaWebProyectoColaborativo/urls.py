from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('personajes/<int:personaje_id>/', views.show_personaje, name='personaje'),
    path('razas/<int:raza_id>/', views.show_raza, name='raza'),
    path('peliculas/<int:pelicula_id>/', views.show_pelicula, name='pelicula'),
    
    path('personajes/', views.index_personajes, name='personajes'),
    path('razas/', views.index_razas, name='razas'),
    path('peliculas/', views.index_peliculas, name='peliculas'),
]

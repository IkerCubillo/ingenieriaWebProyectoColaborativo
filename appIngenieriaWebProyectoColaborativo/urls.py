from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_razas, name='index'),
    path('razas/<int:raza_id>/', views.show_raza, name='detail'),
    path('razas/<int:raza_id>/personajes', views.index_personajes, name='personajes'),
    path('personajes/<int:personaje_id>', views.show_personaje, name='personaje'),
    path('peliculaes/<int:pelicula_id>', views.show_pelicula, name='pelicula'),
]
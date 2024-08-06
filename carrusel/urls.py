from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name='carrusel'),
    path('crear-carrusel', views.createView, name='crear-carrusel'),
    path('editar-carrusel/<int:pk>/', views.editView, name='editar-carrusel'),   
    path('eliminar-carrusel/<int:pk>/', views.deleteView, name='eliminar-carrusel'),
]
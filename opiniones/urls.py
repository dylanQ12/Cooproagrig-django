from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name='opiniones'),
    path('crear-opinion', views.createView, name='crear-opinion'),
    path('editar-opinion/<int:pk>/', views.editView, name='editar-opinion'),
    path('eliminar-opinion/<int:pk>/', views.deleteView, name='eliminar-opinion')
]


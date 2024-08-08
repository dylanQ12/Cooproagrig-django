from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name='produccion'),
    path('crear-produccion', views.createView, name='crear-produccion'),
    path('editar-produccion/<int:pk>/', views.editView, name='editar-produccion'),
    path('eliminar-produccion/<int:pk>/', views.deleteView, name='eliminar-produccion')
]
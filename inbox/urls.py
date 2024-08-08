from django.urls import path
from . import views

urlpatterns = [
    path('', views.inboxView, name='inbox'),
    path('eliminar-mensaje/<int:pk>/', views.deleteMessage, name='eliminar-mensaje')
]
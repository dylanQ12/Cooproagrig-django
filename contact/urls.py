from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacView, name='contact'),
    path('enviar-mensaje', views.formContactView, name='enviar-mensaje')
]
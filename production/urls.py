from django.urls import path
from . import views

urlpatterns = [
    path('', views.productionView, name='production'),
]

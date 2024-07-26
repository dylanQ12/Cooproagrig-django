from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls') ),
    path('acerca-de/', include('about.urls') ),
    path('producción/', include('production.urls') ),
    path('capacitaciones/', include('training.urls') ),
    path('contáctanos/', include('contact.urls') ),
    path('dashboard/', include('dashboard.urls') ),
]

#from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('home.urls') ),
    path('acerca-de/', include('about.urls') ),
    path('producción/', include('production.urls') ),
    path('contáctanos/', include('contact.urls') ),
    path('dashboard/', include('dashboard.urls') ),
    path('login/', include('login.urls') ),
    path('mi-perfil/', include('myprofile.urls') ),
    path('carrusel/', include('carrusel.urls') ),
    path('opiniones/', include('opiniones.urls') ),
    path('produccion/', include('produccionOrganica.urls') ),
    path('inbox/', include('inbox.urls') )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
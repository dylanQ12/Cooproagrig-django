from carrusel.models import Carousel

def all_data(request): 
    context = {
        'carrusel': Carousel.objects.all(),
    }
    return context
    
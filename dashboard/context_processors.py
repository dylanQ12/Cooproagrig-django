from carrusel.models import Carousel

def counts(request):
    context = {
        'carrusel_count': Carousel.objects.count(),
    }
    return context
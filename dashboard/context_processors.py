from carrusel.models import Carousel
from opiniones.models import Opinion
from produccionOrganica.models import ProductionOrganic
from inbox.models import Inbox

def counts(request):
    context = {
        'carrusel_count': Carousel.objects.count(),
        'opiniones_count': Opinion.objects.count(),
        'produccion_count': ProductionOrganic.objects.count(),
        'inbox_count': Inbox.objects.count()
    }
    return context
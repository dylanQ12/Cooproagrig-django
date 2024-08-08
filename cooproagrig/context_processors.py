from carrusel.models import Carousel
from opiniones.models import Opinion
from produccionOrganica.models import ProductionOrganic
from inbox.models import Inbox

def all_data(request): 
    context = {
        'carrusel_items': Carousel.objects.all(),
        'opinion_items': Opinion.objects.all(),
        'produccion_items': ProductionOrganic.objects.all(),
        'inbox_items': Inbox.objects.all().order_by('id')[:5],
    }
    return context
    
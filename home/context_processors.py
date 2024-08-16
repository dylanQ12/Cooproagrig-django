from datetime import datetime

# Fecha actual
def current_year(request):
    return { "current_year": datetime.now().year }

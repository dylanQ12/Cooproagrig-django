from django.shortcuts import render

# Create your views here.
def homeView(request):
    context = {
        'page_title': 'Inicio - Cooproagrig | Cooperativa de Producción Agrícola'
    }
    return render(request, 'home.html', context)

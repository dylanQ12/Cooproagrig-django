from django.shortcuts import render

# Create your views here.
def productionView(request):
    context = {
        'page_title': 'Producción Órganica - Cooproagrig | Cooperativa de Producción Ágricola'
    }
    return render(request, 'production.html', context)

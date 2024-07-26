from django.shortcuts import render

# Create your views here.
def trainingView(request):
    context = {
        'page_title': 'Capacitaciones - Cooproagrig | Cooperativa de Producción Ágricola'
    }
    return render(request, 'training.html', context)
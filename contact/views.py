from django.shortcuts import render

# Create your views here.
def contacView(request):
    context = {
        'page_title': 'Contáctanos - Cooproagrig | Cooperativa de Producción Ágricola'
    }
    return render(request, 'contact.html', context)
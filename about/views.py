from django.shortcuts import render

# Create your views here.
def aboutView(request):
    context = {
        'page_title': 'Acerca de - Cooproagrig | Cooperativa de Producción Ágricola'
    }
    return render(request, 'about.html', context)
    

from django.shortcuts import render
from inbox.models import Inbox
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def contacView(request):
    context = {
        "page_title": "Contáctanos - Cooproagrig | Cooperativa de Producción Agrícola"
    }
    return render(request, "contact.html", context)


@csrf_exempt
def formContactView(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        nombre = request.POST.get("nombre")
        email = request.POST.get("correo")
        mensaje = request.POST.get("message")

        if nombre and email and mensaje:
            contact_item = Inbox(nombre=nombre, email=email, mensaje=mensaje)
            contact_item.save()
            return JsonResponse( {"success": True, "redirect_url": "/contáctanos/"} )
        return JsonResponse( {"success": False, "error": "Missing fields"} )
    
    return render(request, 'contact.html')

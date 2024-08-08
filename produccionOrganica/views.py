from django.shortcuts import render, get_object_or_404
from .models import ProductionOrganic
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def listView(request):
    production_items = ProductionOrganic.objects.all()
    context = {
        "title": "Producción Órganica", 
        "production_items": production_items
    }
    return render(request, "list-production.html", context)


@login_required
def createView(request):
    if (
        request.method == "POST"
        and request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        foto = request.FILES.get("foto")

        if titulo and descripcion and foto:
            produccion_item = ProductionOrganic(
                titulo=titulo, descripcion=descripcion, foto=foto
            )
            produccion_item.save()
            return JsonResponse( {"success": True, "redirect_url": "/produccion/"} )
        return JsonResponse( {"success": False} )

    context = {"title": "Crear Producción"}
    return render(request, "crear-production.html", context)


@login_required
def editView(request, pk):
    produccion_item = get_object_or_404(ProductionOrganic, pk=pk)

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        foto = request.FILES.get("foto", None)

        if titulo and descripcion:
            produccion_item.titulo = titulo
            produccion_item.descripcion = descripcion
            if foto:
                produccion_item.foto = foto
            produccion_item.save()
            return JsonResponse( {"success": True, "redirect_url": "/produccion/"} )
        return JsonResponse( {"success": False} )

    context = {
        "title": "Editar Producción", 
        "produccion_item": produccion_item
    }
    return render(request, "editar-production.html", context)


@login_required
def deleteView(request, pk):
    if request.method == "POST":
        produccion_item = get_object_or_404(ProductionOrganic, pk=pk)
        produccion_item.delete()
        return JsonResponse( {"success": True} )
    return JsonResponse( {"success": False}, status=400 )

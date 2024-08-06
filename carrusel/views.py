from django.shortcuts import redirect, render, get_object_or_404
from carrusel.models import Carousel
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def listView(request):
    carousel_items = Carousel.objects.all()
    success = request.GET.get("success", False)

    context = {
        "title": "Carrusel",
        "carousel_items": carousel_items,
    }
    return render(request, "list-carrusel.html", context)


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
            carousel_item = Carousel(titulo=titulo, descripcion=descripcion, foto=foto)
            carousel_item.save()
            return JsonResponse({"success": True, "redirect_url": "/carrusel/"})
        return JsonResponse({"success": False})

    context = {"title": "Crear Carrusel"}
    return render(request, "crear-carrusel.html", context)


@login_required
def editView(request, pk):
    carousel_item = get_object_or_404(Carousel, pk=pk)

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        foto = request.FILES.get("foto", None)

        if titulo and descripcion:
            carousel_item.titulo = titulo
            carousel_item.descripcion = descripcion
            if foto:
                carousel_item.foto = foto
            carousel_item.save()
            return JsonResponse({"success": True, "redirect_url": "/carrusel/"})
        return JsonResponse({"success": False})

    context = {"title": "Editar Carrusel", "carousel_item": carousel_item}
    return render(request, "editar-carrusel.html", context)


def deleteView(request, pk):
    if request.method == "POST":
        carousel_item = get_object_or_404(Carousel, pk=pk)
        carousel_item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

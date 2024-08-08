from django.shortcuts import render, get_object_or_404
from opiniones.models import Opinion
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def listView(request):
    opinion_items = Opinion.objects.all()
    context = {
        "title": "Opiniones",
        "opinion_items": opinion_items,
    }
    return render(request, "list-opinion.html", context)

@login_required
def createView(request):
    if (
        request.method == "POST"
        and request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):
        nombre_completo = request.POST.get("nombre")
        comentario = request.POST.get("comentario")
        foto = request.FILES.get("foto")

        if nombre_completo and comentario and foto:
            opinion_item = Opinion(nombre_completo=nombre_completo, comentario=comentario, foto=foto)
            opinion_item.save()
            return JsonResponse( {"success": True, "redirect_url": "/opiniones/"} )
        return JsonResponse( {"success": False} )

    context = {"title": "Crear Opinión"}
    return render(request, "crear-opinion.html", context)


def editView(request, pk):
    opinion_item = get_object_or_404(Opinion, pk=pk)

    if request.method == "POST":
        nombre_completo = request.POST.get("nombre")
        comentario = request.POST.get("comentario")
        foto = request.FILES.get("foto", None)

        if nombre_completo and comentario:
            opinion_item.nombre_completo = nombre_completo
            opinion_item.comentario = comentario
            if foto:
                opinion_item.foto = foto
            opinion_item.save()
            return JsonResponse({"success": True, "redirect_url": "/opiniones/"})
        return JsonResponse({"success": False})

    context = {"title": "Editar Opinión", "opinion_item": opinion_item}
    
    
    return render(request, "editar-opinion.html", context)

def deleteView(request, pk):
    if request.method == "POST":
        opinion_item = get_object_or_404(Opinion, pk=pk)
        opinion_item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

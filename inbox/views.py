from django.shortcuts import render, get_object_or_404
from .models import Inbox
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def inboxView(request):
    context = {
        "title": "Inbox",
        "messages": Inbox.objects.all(),
    }
    return render(request, "inbox.html", context)


@login_required
def deleteMessage(request, pk):
    if request.method == "POST":
        inbox_item = get_object_or_404(Inbox, pk=pk)
        inbox_item.delete()
        return JsonResponse( {"success": True} )
    return JsonResponse( {"success": False}, status=400 )

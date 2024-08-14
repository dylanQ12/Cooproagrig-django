from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def loginView(request):
    context = {
        "page_title": "Iniciar sesión - Cooproagrig | Cooperativa de Producción Agrícola"
    }

    if request.method == "POST":
        username = request.POST.get("usuario")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            context['error'] = "¡Nombre de usuario o clave incorrectos!"
            context['attempted'] = True  # Solo se establece si hubo un intento fallido de inicio de sesión.
    else:
        context['attempted'] = False  # Explicitamente definido como False si es una solicitud GET
    
    return render(request, "login.html", context)


# Vista del Logout para cerrar sesión.
def logoutView(request):
    logout(request)
    return redirect("home")

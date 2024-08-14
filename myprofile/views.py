from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.
@login_required
def profileView(request): 
    
    user = request.user
       
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "¡Las claves no coinciden!")
        elif len(password1) < 8:
            messages.error(request, "¡Debe tener al menos 8 caracteres!")
        else:
            user = request.user
            user.username = username
            user.set_password(password1)
            user.save()
            update_session_auth_hash(
                request, user
            )
            # Mantener la sesión después de cambiar la contraseña
            messages.success(request, "¡Guardado satisfactoriamente!")
            #return redirect("dashboard")
    
    # Rol de usuario.
    if user.is_staff:
        role = "Administrador"
    else:
        role = "Visitante"
    
    context = {
        "title": "Mi perfil",
        "username": request.user.username,
        "email": request.user.email,
        "role": role,
    }
    return render(request, "myprofile.html", context)

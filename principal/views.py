from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from firebase_admin import auth

def home(request):
    return render(request, 'home.html')  # Asegúrate de que este archivo existe en "principal/templates/"

def login_view(request):
    if request.method == "POST":
        id_token = request.POST.get("idToken")  # Token enviado desde el frontend
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']

            # Aquí puedes manejar roles según la información en Firebase
            # Por ejemplo, podrías verificar si el usuario es admin
            
            return redirect("dashboard")  # Redirigir al dashboard tras iniciar sesión
        except Exception as e:
            print("Error al verificar token:", e)
            return render(request, "login.html", {"error": "Error en la autenticación"})
            
    return render(request, "login.html")

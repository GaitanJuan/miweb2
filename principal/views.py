from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Cargar la plantilla HTML

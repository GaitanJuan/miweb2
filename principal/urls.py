from django.urls import path
from .views import home, login_view  # Importar todas las vistas necesarias

urlpatterns = [
    path('', home, name='home'),  # Ruta principal que carga index.html
    path('login/', login_view, name='login'),  # Ruta de inicio de sesión
]

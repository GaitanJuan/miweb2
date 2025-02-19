from django.contrib import admin
from django.urls import path
from principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ruta principal
]

from django.urls import path
from .views import login_view

urlpatterns = [
    path("login/", login_view, name="login"),
]

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Ahora la raíz ("/") mostrará index.html
]

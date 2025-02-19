from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← Esto enlaza la vista a "/"
]

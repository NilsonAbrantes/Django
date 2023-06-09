from django.urls import path

from recipes.views import buscar_dados, home

urlpatterns = [
    path("", home),  # HOME
    path("buscar/", buscar_dados, name="buscar_dados"),
]

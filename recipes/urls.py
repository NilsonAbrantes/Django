from django.urls import path

from recipes.views import buscar_dados, home, ship

urlpatterns = [
    path("", home),  # HOME
    path("buscar/", buscar_dados, name="buscar_dados"),
    path("new-ship/", ship, name="ship"),
]

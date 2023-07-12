from django.urls import path

from Ships.views import buscar_dados, home, ship, atracados, fundeados, esperando


urlpatterns = [
    path("", home),  # HOME
    path("buscar/", buscar_dados, name="buscar_dados"),
    path("new-ship/", ship, name="ship"),
    path("atracados/", atracados, name="atracados"),
    path("fundeados/", fundeados, name="fundeados"),
    path("esperando/", esperando, name="esperando"),
]


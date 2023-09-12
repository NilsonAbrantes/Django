from django.urls import path

from Ships.views import (
    atracados,
    buscar_dados,
    esperando,
    fundeados,
    home,
    ship,
    simulation,
)

urlpatterns = [
    path("", home),
    path("buscar/", buscar_dados, name="buscar_dados"),
    path("new-ship/", ship, name="ship"),
    path("atracados/", atracados, name="atracados"),
    path("fundeados/", fundeados, name="fundeados"),
    path("esperando/", esperando, name="esperando"),
    path("simulation/", simulation, name="simulation"),
    path("simulation-view/", simulation, name="simulationview"),
]

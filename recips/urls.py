from django.urls import path

from recips.views import contato, home, sobre

urlpatterns = [
    path("", home),  # HOME
    path("sobre/", sobre),  # /sobre
    path("contato/", contato),  # /contato
]
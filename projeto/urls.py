from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Ships.urls")),  # HOME
    path("buscar/", include("Ships.urls")),
    path("new-ship/", include("Ships.urls")),
    path("atracados/", include("Ships.urls")),
    path("fundeados/", include("Ships.urls")),
    path("esperando/", include("Ships.urls")),
]

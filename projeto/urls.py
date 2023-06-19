from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("recipes.urls")),  # HOME
    path("buscar/", include("recipes.urls")),
    path("new-ship/", include("recipes.urls")),
]

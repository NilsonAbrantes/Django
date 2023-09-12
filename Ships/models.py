from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class New_ship(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField()
    qtd_carga = models.FloatField()
    dwt = models.FloatField()
    IMO = models.IntegerField()
    cad_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # noqa: E501
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

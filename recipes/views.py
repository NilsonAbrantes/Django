import csv

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "recipes/pages/home.html")


def buscar_dados(request):
    if request.method == "POST":
        termo_busca = request.POST.get("termo_busca")
        resultados = []
        if termo_busca:
            termo_busca = termo_busca.upper()
            with open("recipes/navios_fundeados.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if termo_busca in row["Navio"]:
                        resultados.append(row)

        return render(
            request, "recipes/partials/resultado_busca.html", {"resultados": resultados}
        )

    return render(request, "recipes/pages/home.html")

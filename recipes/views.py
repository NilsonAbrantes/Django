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
            with open("recipes/result.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if termo_busca in row["Navio"]:
                        resultados.append(row)
                    elif termo_busca in row["IMO"]:
                        resultados.append(row)

        return render(
            request, "recipes/partials/search_result.html", {"resultados": resultados}
        )

    return render(request, "recipes/pages/home.html")


def ship(request):
    if request.method == "POST":
        #recolhendo os dados inseridos no site
        Situation = request.POST.get("situacao")
        Imo = request.POST.get("imo")
        Navio = request.POST.get("navio")
        Operation = request.POST.get("op")
        Length = request.POST.get("comp")
        Dwt = request.POST.get("dwt")
        Charge = request.POST.get("carga")
        Qtd_Charge = request.POST.get("qtd_carga")
        Shut_up = request.POST.get("calado")
        Agency = request.POST.get("agencia")
        
        #Transformando os dados recebidos em maiusculo
        Situation = Situation.upper()
        Navio = Navio.upper()
        Operation = Operation.upper()
        Length = Length.upper()
        Charge = Charge.upper()
        Shut_up = Shut_up.upper()
        Agency = Agency.upper()
        
        # Lista com os dados a serem escritos no CSV
        data = [Situation, Imo, Navio, Operation, Length, Dwt, Charge, Qtd_Charge, Shut_up, Agency]
        
        # Caminho do arquivo CSV onde os dados serão escritos
        csv_file = "recipes/test.csv"
        
        # Escrevendo os dados no arquivo CSV
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)


        return render(request, "recipes/pages/add_ship.html")

    return render(request, "recipes/pages/add_ship.html")


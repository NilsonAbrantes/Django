import csv

from django.shortcuts import render
# from .models import New_ship


# Create your views here.
def home(request):
    return render(request, "Ships/pages/home.html")


def buscar_dados(request):
    if request.method == "POST":
        termo_busca = request.POST.get("termo_busca")
        resultados = []
        if termo_busca:
            termo_busca = termo_busca.upper()
            with open("Ships/result.csv", "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if termo_busca in row["Navio"]:
                        resultados.append(row)
                    elif termo_busca in row["IMO"]:
                        resultados.append(row)

        return render(
            request, "Ships/partials/search_result.html", {"resultados": resultados}  # noqa: E501
        )

    return render(request, "Ships/pages/home.html")


def ship(request):
    error_message = None
    if request.method == "POST":
        # recolhendo os dados inseridos no site
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

        # Transformando os dados recebidos em maiusculo
        Situation = Situation.upper()
        Navio = Navio.upper()
        Operation = Operation.upper()
        Length = Length.upper()
        Charge = Charge.upper()
        Shut_up = Shut_up.upper()
        Agency = Agency.upper()

        # Lista com os dados a serem escritos no CSV
        data = [
            Situation,
            Imo,
            Navio,
            Operation,
            Length,
            Dwt,
            Charge,
            Qtd_Charge,
            Shut_up,
            Agency,
        ]
        # Calculo de Risco
        data_result = []
        Dwt = float(Dwt)
        Qtd_Charge = float(Qtd_Charge)
        Deslastre_form = ((Dwt - Qtd_Charge) * 0.3) * 1000
        Deslastre_form = float(Deslastre_form)
        Deslastre = "{:.2f}".format(Deslastre_form)
        Deslastre = float(Deslastre)
        if Deslastre < 1500:
            data_result = [
                Situation,
                Navio,
                Deslastre,
                "0.5",
                "BAIXO",
                Imo,
            ]
        elif Deslastre <= 5000:
            data_result = [
                Situation,
                Navio,
                Deslastre,
                "1",
                "BAIXO",
                Imo,
            ]
        else:
            data_result = [
                Situation,
                Navio,
                Deslastre,
                "2",
                "MÉDIO",
                Imo,
            ]
        if Situation == "NONE":
            error_message = "Favor preencha os campos obrigatórios."
            return render(
                request, "Ships/pages/add_ship.html", {"error_message": error_message}  # noqa: E501
            )

        # Caminho do arquivo CSV onde os dados serão escritos
        csv_file = "Ships/test.csv"
        csv_file_result = "Ships/result.csv"

        # Escrevendo os dados no arquivo CSV
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)

        # Escrevendo resultados no arquivo CSV
        with open(csv_file_result, mode="a", encoding="utf-8", newline="") as file_result:  # noqa: E501
            writer = csv.writer(file_result)
            writer.writerow(data_result)

        return render(request, "Ships/pages/add_ship.html")

    return render(request, "Ships/pages/add_ship.html")


def atracados(request):
    navios_atracados = []
    with open("Ships/result.csv", "r") as csvfile:
        reader1 = csv.DictReader(csvfile)
        reader1 = sorted(reader1, key=lambda row: row['Navio'])
        for row in reader1:
            navios_atracados.append(row)
    return render(
        request, "Ships/partials/atracados.html", {"navios_atracados": navios_atracados}  # noqa: E501
    )


def fundeados(request):
    navios_fundeados = []
    with open("Ships/result.csv", "r") as csvfile:
        reader2 = csv.DictReader(csvfile)
        for row in reader2:
            navios_fundeados.append(row)
    return render(
        request, "Ships/partials/fundeados.html", {"navios_fundeados": navios_fundeados}  # noqa: E501
    )


def esperando(request):
    navios_esperando = []
    with open("Ships/result.csv", "r") as csvfile:
        reader3 = csv.DictReader(csvfile)
        for row in reader3:
            navios_esperando.append(row)
    return render(
        request, "Ships/partials/esperando.html", {"navios_esperando": navios_esperando}  # noqa: E501
    )


def simulation(request):
    error_message = None
    if request.method == "POST":
        # recolhendo os dados inseridos no site
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

        # Transformando os dados recebidos em maiusculo
        Situation = Situation.upper()
        Navio = Navio.upper()
        Operation = Operation.upper()
        Length = Length.upper()
        Charge = Charge.upper()
        Shut_up = Shut_up.upper()
        Agency = Agency.upper()

        Dwt = float(Dwt)
        Qtd_Charge = float(Qtd_Charge)
        Deslastre_form = ((Dwt - Qtd_Charge) * 0.3) * 1000
        Deslastre_form = float(Deslastre_form)
        Deslastre = "{:.2f}".format(Deslastre_form)
        Deslastre = float(Deslastre)
        if Deslastre < 1500:
            data_row = [
                Situation,
                Imo,
                Navio,
                Operation,
                Length,
                Dwt,
                Charge,
                Qtd_Charge,
                Shut_up,
                Agency,
                Deslastre,
                "0.5",
                "BAIXO",
            ]
        elif Deslastre <= 5000:
            data_row = [
                Situation,
                Imo,
                Navio,
                Operation,
                Length,
                Dwt,
                Charge,
                Qtd_Charge,
                Shut_up,
                Agency,
                Deslastre,
                "1",
                "BAIXO",
            ]
        elif Deslastre > 5000:
            data_row = [
                Situation,
                Imo,
                Navio,
                Operation,
                Length,
                Dwt,
                Charge,
                Qtd_Charge,
                Shut_up,
                Agency,
                Deslastre,
                "2",
                "MÉDIO",
            ]
        data_simulation = [
            "Situacao",
            "IMO",
            "Navio",
            "Operação",
            "Comprimento",
            "Dwt",
            "Carga",
            "Qtd_carga",
            "Calado",
            "Agência",
            "Deslastre",
            "Pontos",
            "Risco",
        ]
        # Lista com os dados a serem escritos no CSV
        if Situation == "NONE":
            error_message = "Favor preencha os campos obrigatórios."
            return render(
                request, "Ships/pages/simulation.html", {"error_message": error_message}  # noqa: E501
            )

        # Caminho do arquivo CSV onde os dados serão escritos
        csv_file = "Ships/simu.csv"

        # Escrevendo os dados no arquivo CSV
        with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data_simulation)
            writer.writerow(data_row)

        simu_view = []
        with open("Ships/simu.csv", "r") as csvfile1:
            reader2 = csv.DictReader(csvfile1)
            for row in reader2:
                simu_view.append(row)
        return render(
            request, "Ships/partials/simulation-view.html", {"simu_view": simu_view}  # noqa: E501
        )

    return render(request, "Ships/pages/simulation.html")


def simulationview(request):
    return render(request, "Ships/partials/simulation-view.html")

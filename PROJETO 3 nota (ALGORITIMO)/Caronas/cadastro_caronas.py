import os
caronas = [{
            'nomedomotorista': "Gabriel",
            'emailmotorista': "gabriel@gmail.com",
            'veiculo': "FIAT UNO",
            'placa': "ZYT-431",
            'localdeorigem': "sj",
            'destino': "cz",
            'data': "20/12/2006",
            'horario': "14.10",
            'quantidadedevagas': "2",
            'reserva': [],
            'valorporvaga': "10",
            },
            {
            'nomedomotorista': "Gabriel",
            'emailmotorista': "gabriel@gmail.com",
            'veiculo': "FIAT UNO",
            'placa': "ZYT-431",
            'localdeorigem': "sao joao do rio do peixe",
            'destino': "cajazeiras",
            'data': "20/12/2006",
            'horario': "14.10",
            'quantidadedevagas': "2",
            'reserva': [],
            'valorporvaga': "10",
            },
            {'nomedomotorista': "Lucas",
            'emailmotorista': "lucas@gmail.com",
            'veiculo': "SKLINE",
            'placa': "SKE-223",
            'localdeorigem': "cz",
            'destino': "baixio",
            'data': "21/06/2025",
            'horario': "17.20",
            'quantidadedevagas': "3",
            'reserva': [],
            'valorporvaga': "10",
          },]

def cadastrar_caronas():
        nomedri = input("Digite o seu nome de motorista: ")
        emailmoto = input("Digite o seu email para o cadastro da carona: ").lower()
        veiculocad = input("Digite o nome do seu veículo para o cadastro da carona: ").upper()
        placacad = input("Digite o nome da placa do seu veículo para o cadastro da carona: ").upper()
        locorg = input("Digite o local de origem da sua carona: ").lower().strip()
        destiny = input("Digite o local de destino da carona: ").lower().strip()
        data = input("Digite a data da sua carona no padrão (dd/mm/aaaa): ")
        time = float(input("Digite o horário da sua carona em formato (24h): "))
        quavag = int(input("Digite a quantidade de vagas da sua carona: "))
        reservas = input("Digite se já houver alguma reserva feita antes do cadastro: ").lower()
        valpvag = float(input("Digite o valor por vaga da sua carona: "))
        print("Carona Cadastrada com sucesso!")
        os.system('cls' if os.name == 'nt' else 'clear')
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:10])
        validado = "S"
        eBissexto = "N"
        if(ano % 4 == 0):
            eBissexto = "S"
        if(ano % 100 == 0 and ano % 400 != 0):
            eBissexto = "N"
        if(mes == 1 
        or mes == 3 
        or mes == 5 
        or mes == 7
        or mes == 8
        or mes == 10
        or mes == 12):
            if(dia >= 1 and dia <= 31):
                validado = 'S'
        elif(mes == 4 
            or mes == 6 
            or mes == 9 
            or mes == 11):
                if(dia >= 1 and dia <= 30):
                    validado = 'S'
        elif(mes == 2):
            if(eBissexto == 'S' and dia >= 1 and dia <= 29):
                validado = 'S'
            elif(dia >= 1 and dia <= 28):
                validado = 'S'
        if(validado == "S"):
            caronareg = {
                'nomedomotorista': nomedri,
                'emailmotorista': emailmoto,
                'veiculo': veiculocad,
                'placa': placacad,
                'localdeorigem': locorg,
                'destino': destiny,
                'data': data,
                'horario': time,
                'quantidadedevagas': quavag,
                'reserva': reservas,
                'valorporvaga': valpvag,
            }
            caronas.append(caronareg)
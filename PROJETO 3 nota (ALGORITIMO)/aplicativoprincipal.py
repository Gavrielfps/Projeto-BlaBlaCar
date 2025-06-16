import os
usuarios = [{
             "nome": "Yasmin",
             "email": "yasmin@gmail.com",
             "senha": "2",
             "telefone": "(83)9999999999",
             "endereco": "Rua: ALEAROTIO222",
             "tipo": "passageiro",
},]
drivers = [{"nome": "Gabriel", "email": "gabriel@gmail.com", "senha": "1", "telefone": "(83)8888888888", "endereco": "Rua: 999", "veiculo": "FIAT UNO", "placa": "zyt-431", "tipo": "motorista",},
           {"nome": "Lucas", "email": "lucas@gmail.com", "senha": "7", "telefone": "(83)7777777777", "endereco": "Rua: BR201", "veiculo": "SKYLINE", "placa": "SKE-223", "tipo": "motorista",},
          ]
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

while True:
    largura = 70
    titulo = ("""
        ______
       /|_||_\\`.__
      (   _    _ _\\
______=`-(_)--(_)-'___________________________________________________________________

██████╗ ██╗      █████╗ ██████╗ ██╗      █████╗  ██████╗ █████╗ ██████╗ 
██╔══██╗██║     ██╔══██╗██╔══██╗██║     ██╔══██╗██╔════╝██╔══██╗██╔══██╗
██████╔╝██║     ███████║██████╔╝██║     ███████║██║     ███████║██████╔╝
██╔══██╗██║     ██╔══██║██╔══██╗██║     ██╔══██║██║     ██╔══██║██╔══██╗
██████╔╝███████╗██║  ██║██████╔╝███████╗██║  ██║╚██████╗██║  ██║██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
""")
    print()
    print("=" * largura)
    print(titulo)
    print("=" * largura)
    print()
    login = {}
    caronapdriver = {}

    escolha = input("Bem-Vindo(a)\n\n" \
                     "Escolha uma das opcões disponíveis:\n\n" \
                     "1 - Cadastrar Usuário\n" \
                     "2 - Cadastrar Motorista\n" \
                     "3 - Login de Usuário\n" \
                     "0 - Logout\n\nOpção:"
                     )
    if(escolha == "0"):
        break
    
    if(escolha == "1"):
       nome = input("Digite o seu nome completo: ")
       email = input("Digite o seu email: ").lower()
       senha = input("Digite a sua senha: ").lower()
       telefone = input("Digite seu telefone: ")
       endereco = input("Digite seu endereço: ").lower()
       if("@" not in email or ".com" not in email):
            print("O email digitado é inválido. Digite usando '@' e '.com' para conseguir se registrar e prosseguir!")
       emailexiste = False
       for usu in usuarios:
           if(email == usu['email'].lower()):
             emailexiste = True
             print("O email já está cadastrado! Tente usar outro.\n")
             break
       if(not emailexiste):
         usuarios.append({'nome':nome, 'email':email, 'senha':senha, 'telefone': telefone, 'endereco': endereco, 'tipo': 'passageiro'})
         print("Usuário cadastrado com sucesso!\n")
         print(f"Dados de usuário: {nome}, {email}")
         input("Clique no Enter para continuar . . .")
         os.system('cls' if os.name == 'nt' else 'clear')

    if(escolha == "2"):
       nome = input("Digite o seu nome completo: ")
       email = input("Digite o seu email: ").lower()
       senha = input("Digite a sua senha: ").lower()
       telefone = input("Digite o número do seu telefone: ")
       endereco = input("Digite o seu endereço: ").lower()     
       veiculo = input("Digite o modelo do seu veículo: ").upper()
       placa = input("Digite a placa do seu veículo: ").upper()
       if("@" not in email or ".com" not in email):
            print("O email inserido é inválido. Digite usando '@' e '.com' para conseguir se registrar e prosseguir!")
       else:
           print("Usuário cadastrado com sucesso!\n") 
           print(f"Dados do usuário: {nome}, {email}")
           input("Clique no Enter para continuar . . .")
       emailexiste = False
       for dri in drivers:
           if(email == dri['email']):
               emailexiste = True
               print("O email já está cadastrado! Tente usar outro.\n")
               break
       drivers.append({'nome':nome, 'email':email, 'senha':senha, 'telefone': telefone, 'endereco': endereco, 'veiculo': veiculo, 'placa': placa, 'tipo': 'motorista', "avaliacao": "[]",},)
       os.system('cls' if os.name == 'nt' else 'clear')

    if(escolha == "3"):
        loging = False
        while True:
            email = input("Digite o seu email: ").strip().lower()
            senha = input("Digite a sua senha: ").strip().lower()
            encontradousu = False
            encontradodri = False
            for usu in usuarios:
                if(email == usu['email'] and senha == usu['senha'] and usu['tipo'] == "usuario"):
                    encontradousu = True
                    loging = True
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("-" * 50)
                    print("-" * 50)
                    print("Login efetuado. . .\n")
                    print(f"Usuário: {usu['nome']} efetuou o login com sucesso!\n")
                    print(f"Bem-Vindo(a)")
                    print("-" * 50)
                    menuon = False
                    while True:
                        escolhausu = input("Escolha uma das opções abaixo:\n\n" \
                                            "1 - Listar Caronas disponíveis\n" \
                                            "2 - Buscar uma Carona da origem ao destino\n" \
                                            "3 - Reservar uma vaga em Carona\n" \
                                            "4 - Cancelar uma Carona\n" \
                                            "5 - Mostrar detalhes de uma Carona específica\n" \
                                            "0 - Voltar para o menu inicial\n\nOpção:" 
                                        )
                        
                        if(escolhausu == "0"):
                            menuon = False
                            print("-" * 50)
                            print("Logout efetuado com sucesso!\n\n")
                            input("Aperte no Enter para voltar ao menu inicial . . .")
                            print("-" * 50)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
        
                        if(escolhausu == '1'):
                            for c in caronas:
                                print("-" * 50)
                                print(f"Motorista: {c['nomedomotorista']}")
                                print(f"Email: {c['emailmotorista']}")
                                print(f"Veículo: {c['veiculo']}, Placa: {c['placa']}")
                                print(f"Origem: {c['localdeorigem']}")
                                print(f"Destino: {c['destino']}")
                                print(f"Data: {c['data']}")
                                print(f"Horário: {c['horario']}")
                                print(f"Quantidade de vagas: {c['quantidadedevagas']}")
                                print(f"Pessoas com vaga reservadas: {c['reserva']}")
                                print(f"Valor da vaga por pessoa: {c['valorporvaga']}")
                                print("-" * 50)

                        elif(escolhausu == '2'):
                            perorig = input("Digite o local de origem: ").lower()
                            perdest = input("digite o local de destino: ").lower()
                            encontradacarona = False
                            for carona in caronas:
                                if(carona['localdeorigem'] == perorig and carona['destino'] == perdest):
                                    encontradacarona = True
                                    print("-" * 50)
                                    print(f"Motorista: {carona['nomedomotorista']}")
                                    print(f"Email: {carona['emailmotorista']}")
                                    print(f"Veículo: {carona['veiculo']}, Placa: {carona['placa']}")
                                    print(f"Data: {carona['data']}, Horário: {carona['horario']}")
                                    print(f"Vagas disponíveis: {carona['quantidadedevagas']}")
                                    print(f"Valor por vaga: {carona['valorporvaga']}")
                                    print("-" * 50)
                            if(not encontradacarona):
                                print("Nenhuma carona encontrada com esses dados. Tente novamente.\n")

                        elif(escolhausu == '3'):
                            emailmotorista3 = input("Digite o email do motorista para reservar a carona: ").lower()
                            datacarona3 = input("Digite a data da carona desejada: ")
                            confirmacaores3 = input("Deseja reservar a carona? (S / N): ").upper()
                            emailencontrado3 = False
                            caronaencontrada3 = False
                            for dri in drivers:
                                if(emailmotorista3 == dri['email']):
                                    emailencontrado3 = True
                                    for d in caronas:
                                        if(d["data"] == datacarona3 and d["emailmotorista"] == emailmotorista3):
                                            caronaencontrada3 = True
                                            if(confirmacaores3 == 'S'):
                                                if(d["data"] == datacarona3 and d["emailmotorista"] == emailmotorista3):
                                                    if(int(d["quantidadedevagas"]) > 0):
                                                        if(usu["nome"] not in d["reserva"]):
                                                            d["reserva"].append(usu["nome"])
                                                            d["quantidadedevagas"] = str(int(d["quantidadedevagas"]) - 1)
                                                            print("Carona reservada com sucesso!\n")
                                                        else:
                                                            print("Você já reservou essa carona.\n")
                                                    else:
                                                        print("Não há mais vagas disponíveis.\n")
                                            else:
                                                print("Reserva de Carona Cancelada com Sucesso!")
                                            break
                                    break
                            if(not emailencontrado3):
                                print("O email do motorista não existe dentro da aplicação! Tente usar um válido dentro das caronas disponíveis!\n")
                            if(not caronaencontrada3):
                                print("Não existe nenhuma carona desse motorista com esta data!\n")

                        elif(escolhausu == "4"):
                            emailmotorista4 = input("Digite o email do motorista para cancelar a carona: ").lower()
                            datacarona4 = input("Digite a data da carona desejada: ")
                            confirmacaores4 = input("Deseja cancelar a carona? (S / N): ").upper()
                            emailencontrado4 = False
                            for dri in drivers:
                                if(emailmotorista4 == dri['email']):
                                    emailencontrado4 = True
                                    caronaencontrada4 = False
                                    for c4 in caronas:
                                        if(datacarona4 == c4["data"] and c4['emailmotorista'] == dri["email"]):
                                            caronaencontrada4 = True
                                            if(confirmacaores4 == 'S'):
                                                    if(int(c4["quantidadedevagas"]) > 0):
                                                        c4["quantidadedevagas"] = int(c4["quantidadedevagas"]) + 1
                                                        if(usu["nome"] in c4["reserva"]):
                                                            c4["reserva"].remove(usu["nome"])
                                                            print("Carona cancelada com sucesso!\n")
                                                        else:
                                                            print("Não há caronas para serem canceladas!\n")
                                                    else:
                                                        if(usu["nome"] in c4["reserva"]):
                                                            c4["quantidadedevagas"] = int(c4["quantidadedevagas"]) + 1
                                                            c4["reserva"].remove(usu["nome"])
                                                            print("Carona cancelada com sucesso!\n")
                                                        else:
                                                            print("Não há caronas para serem canceladas!\n")
                                            else:
                                                print("Você não cancelou a vaga!\n")
                                                break
                                            break
                                        if(not caronaencontrada4):
                                            print("Não existe nenhuma carona desse motorista com essa data!\n")
                                        break
                                if(not emailencontrado4):
                                    print("O email do motorista não existe dentro da aplicação! Tente usar um valido dentro das caronas disponíveis!\n")

                        elif(escolhausu == "5"):
                            emailmotorista5 = input("Digite o email do motorista para mostrar os detalhes da carona: ").lower()
                            datacarona5 = input("Digite a data da carona desejada: ")
                            emailencontrado5 = False
                            for d in drivers:
                                if(emailmotorista5 == d['email']):
                                    emailencontrado5 = True
                                    encontroucarona5 = False
                                    for c in caronas:
                                        if(datacarona5 == c["data"] and d["email"] == emailmotorista5):
                                            print("-" * 50)
                                            print(f"Motorista: {c['nomedomotorista']}")
                                            print(f"Origem: {c['localdeorigem']}")
                                            print(f"Destino: {c['destino']}")
                                            print(f"Veículo: {c['veiculo']}, Placa: {c['placa']}")
                                            print(f"Data: {c['data']}")
                                            print(f"Horário: {c['horario']}")
                                            print(f"Quantidade de vagas: {c['quantidadedevagas']}")
                                            print(f"Pessoas com vaga reservadas: {c['reserva']}")
                                            print(f"Valor da vaga por pessoa: {c['valorporvaga']}")
                                            print("-" * 50)
                                            encontroucarona5 = True
                                    break
                            if(not emailencontrado5):
                                print("O email do motorista está incorreto!\n")
                            elif(not encontroucarona5):
                                print("A data digitada n corresponde com nenhuma das caronas disponíveis!\n")

            else:
                for dri in drivers:
                    if(email == dri['email'] and senha == dri['senha'] and dri['tipo'] == "motorista"):
                        motoristalogado = dri
                        encontradodri = True
                        loginon = True
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("-" * 50)
                        print("Login efetuado. . .\n")
                        print(f"Usuário: {dri['nome']} efetuou o login com sucesso!\n")
                        print("Bem-Vindo(a)")
                        print("-" * 50)
                        while True:
                            escolhadri = input("Escolha uma das opções abaixo:\n\n" \
                                                "1 - Cadastrar uma nova carona\n" \
                                                "2 - Listar Caronas disponíveis\n" \
                                                "3 - Buscar Carona da origem ao destino\n" \
                                                "4 - Excluir Carona\n" \
                                                "5 - Mostrar Caronas cadastradas\n" \
                                                "0 - Logout\n\nOpção:" 
                                            )

                            if(escolhadri == "0"):
                                loginon = False
                                print("-" * 50)
                                print("Logout efetuado com sucesso!\n\n")
                                input("Pressione Enter para voltar ao menu inicial . . .")
                                print("Bem-Vindo(a)")
                                print("-" * 50)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break

                            if(escolhadri == '1'):
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
                        
                            elif(escolhadri == '2'):
                                for c in caronas:
                                    print("-" * 50)
                                    print(f"Motorista: {c['nomedomotorista']}")
                                    print(f"Email: {c['emailmotorista']}")
                                    print(f"Veículo: {c['veiculo']}, Placa: {c['placa']}")
                                    print(f"Origem: {c['localdeorigem']}")
                                    print(f"Destino: {c['destino']}")
                                    print(f"Data: {c['data']}")
                                    print(f"Horário: {c['horario']}")
                                    print(f"Quantidade de vagas: {c['quantidadedevagas']}")
                                    print(f"Pessoas com vaga reservadas: {c['reserva']}")
                                    print(f"Valor da vaga por pessoa: {c['valorporvaga']}")
                                    print("-" * 50)

                            elif(escolhadri == '3'):
                                perorig = input("Digite o local de origem: ").lower().strip()
                                perdest = input("digite o local de destino: ").lower().strip()
                                for carona in caronas:
                                    if(carona['localdeorigem'] == perorig and carona['destino'] == perdest):
                                        encontradacarona = True
                                        print("-" * 50)
                                        print(f"Motorista: {carona['nomedomotorista']}")
                                        print(f"Email: {carona['emailmotorista']}")
                                        print(f"Veículo: {carona['veiculo']}, Placa: {carona['placa']}")
                                        print(f"Data: {carona['data']}, Horário: {carona['horario']}")
                                        print(f"Vagas disponíveis: {carona['quantidadedevagas']}")
                                        print(f"Valor por vaga: {carona['valorporvaga']}")
                                        print("-" * 50)
                                if(not encontradacarona):
                                    print("Nenhuma carona encontrada com esses dados. Tente novamente.\n")

                            elif(escolhadri == '4'):
                                datacaronadriexc = input("Digite a data da carona desejada: ")
                                desicion = input("Você deseja mesmo excluir a sua carona? (S / N): ").upper()
                                if(desicion == "S"):
                                    for c2 in caronas:
                                        if(datacaronadriexc == c2["data"]):
                                            caronas.remove(c2)
                                            print("Carona excluida com sucesso!\n")
                                else:
                                    print("Você não excluiu sua carona!")
    
                            elif(escolhadri == '5'):
                                if(not encontradodri):
                                    print("Você precisa estar logado como motorista para ver suas caronas.\n")
                                else:
                                    caronaencontrada = False
                                    for c in caronas:
                                        if(c["emailmotorista"] == dri["email"]):
                                            print("-" * 50)
                                            print(f"Veículo: {c['veiculo']}, Placa: {c['placa']}")
                                            print(f"Origem: {c['localdeorigem']}")
                                            print(f"Destino: {c['destino']}")
                                            print(f"Data: {c['data']}")
                                            print(f"Horário: {c['horario']}")
                                            print(f"Valor da vaga por pessoa: {c['valorporvaga']}")
                                            print(f"Quantidade de vagas: {c['quantidadedevagas']}")
                                            print(f"Pessoas com vaga reservadas: {c['reserva']}")
                                            print("-" * 50)
                                            caronaencontrada = True
                                if(not caronaencontrada):
                                    print("Você não possui caronas cadastradas.\n")
                else:
                    print("Usuário não existe!\n\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

    if(escolha == "4"):
        print(usuarios)
    if(escolha == "5"):
        print(drivers)
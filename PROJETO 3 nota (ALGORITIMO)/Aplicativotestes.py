import os
from relatorios.relatorio_de_totalizacao import mostrar_relatorio as relatorio_caronas_mostrar
from relatorios.relatorio_de_totalizacao import salvar_relatorio as relatorio_caronas_salvar
from usuarios.passageiros.registro_e_validacao_email import importar_arquivo_dos_passageiros
from usuarios.motoristas.registro_e_validacao_email_motorista import importar_arquivo_dos_motoristas
from relatorios.relatorio_de_totalizacao import mostrar_relatorio
from relatorios.relatorio_de_totalizacao import salvar_relatorio
importar_arquivo_dos_motoristas()
importar_arquivo_dos_passageiros()
import usuarios.passageiros.registro_e_validacao_email as cadastro
import usuarios.motoristas.registro_e_validacao_email_motorista as cadastrodriver
import usuarios.passageiros.login_usu as loginusu
import usuarios.motoristas.login_driver as logindriver
from Caronas.cadastro_caronas import cadastrar_caronas as cadastro_de_caronas
from Caronas.excluir_carona import excluir_a_carona as excluir
from Caronas.listar import listarcaronas as listar
from Caronas.buscar_carona_origem_e_destino import encontrar_carona as encontrar
from Caronas.cancelar_carona import cancelar_carona as cancelar
from Caronas.reserva_de_vaga import reservar_carona as reserva
from Caronas.mostrar_detalhes_carona import mostrar_detalhes_da_carona as detalhes_carona
from Caronas.listar_caronas_individuais import listagem_de_carona_particular as listagem_particular
from usuarios.passageiros.registro_e_validacao_email import usuarios
from usuarios.motoristas.registro_e_validacao_email_motorista import drivers                    

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
    print("VERSÃO ATUALIZADA DO CÓDIGO")
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
                     "4 - Login do Motorista\n" \
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
       if cadastro.cadastro_do_usuario_final(nome, email, senha, telefone, endereco):
            print("Cadastro realizado com sucesso!")
       else:
            print("Falha no cadastro. Verifique os dados.")
    
       input("Pressione Enter para continuar...")

    if(escolha == "2"):
       nome = input("Digite o seu nome completo: ")
       email = input("Digite o seu email: ").lower()
       senha = input("Digite a sua senha: ").lower()
       telefone = input("Digite o número do seu telefone: ")
       endereco = input("Digite o seu endereço: ").lower()     
       veiculo = input("Digite o modelo do seu veículo: ").upper()
       placa = input("Digite a placa do seu veículo: ").upper()
       cadastrodriver.email_invalido_dri_e_cadastro_final(nome, email, senha, telefone, endereco, veiculo, placa)
       cadastrodriver.email_igual_dri(email)
       os.system('cls' if os.name == 'nt' else 'clear')

    if(escolha == "3"):
        loging = False
        while True:
            email = input("Digite o seu email: ").strip().lower()
            senha = input("Digite a sua senha: ").strip().lower()
            loginusu.login_do_usuario(email, senha)
            usuario_logado = loginusu.login_do_usuario(email, senha)
            
            if(usuario_logado):
                os.system('cls' if os.name == 'nt' else 'clear')
                while True:
                    loginon = True
                    escolhausu = input("Escolha uma das opções abaixo:\n\n" \
                                    "1 - Listar Caronas disponíveis\n" \
                                    "2 - Buscar uma Carona da origem ao destino\n" \
                                    "3 - Reservar uma vaga em Carona\n" \
                                    "4 - Cancelar uma Carona\n" \
                                    "5 - Mostrar detalhes de uma Carona específica\n" \
                                    "0 - Voltar para o menu inicial\n\nOpção:" 
                                )
                        
                    if(escolhausu == "0"):
                        loginon = False
                        print("-" * 50)
                        print("Logout efetuado com sucesso!\n\n")
                        input("Pressione Enter para voltar ao menu inicial . . .")
                        print("-" * 50)
                        break


                    if(escolhausu == '1'):
                        listar.listarcaronas()

                    elif(escolhausu == '2'):
                        perorig = input("Digite o local de origem: ").lower()
                        perdest = input("digite o local de destino: ").lower()
                        encontrar.encontrar_carona(perorig, perdest)

                    elif(escolhausu == '3'):
                        emailmotorista3 = input("Digite o email do motorista para reservar a carona: ").lower()
                        datacarona3 = input("Digite a data da carona desejada: ")
                        confirmacaores3 = input("Deseja reservar a carona? (S / N): ").upper()
                        reserva.reservar_carona(emailmotorista3, datacarona3, confirmacaores3)

                    elif(escolhausu == "4"):
                        emailmotorista4 = input("Digite o email do motorista para cancelar a carona: ").lower()
                        datacarona4 = input("Digite a data da carona desejada: ")
                        confirmacaores4 = input("Deseja cancelar a carona? (S / N): ").upper()
                        cancelar.cancelar_carona(emailmotorista4, datacarona4, confirmacaores4)

                    elif(escolhausu == "5"):
                        emailmotorista5 = input("Digite o email do motorista para mostrar os detalhes da carona: ").lower()
                        datacarona5 = input("Digite a data da carona desejada: ")
                        detalhes_carona.mostrar_detalhes_carona(emailmotorista5, datacarona5)
    
                    input("Pressione Enter para continuar...")

                break
            else:
                print("Login falhou. Tente novamente.")
                input("Pressione Enter para continuar...")

    if(escolha == '4'):
        while True:
            email_driver = input("Digite o seu email de motorista: ").strip().lower()
            senha_driver = input("Digite a sua senha: ").strip().lower()
            email_do_motorista_logado = logindriver.login_driver(email_driver, senha_driver)
            if(email_do_motorista_logado):
                while True:
                    loginon = True
                    escolhadri = input("Escolha uma das opções abaixo:\n\n" \
                                         "1 - Cadastrar uma nova carona\n" \
                                         "2 - Listar Caronas disponíveis\n" \
                                         "3 - Buscar Carona da origem ao destino\n" \
                                         "4 - Excluir Carona\n" \
                                         "5 - Mostrar Caronas cadastradas\n" \
                                         "6 - Mostrar Relatorio das Caronas\n" \
                                         "0 - Logout\n\nOpção:" 
                                    )

                    if(escolhadri == "0"):
                        loginon = False
                        print("-" * 50)
                        print("Logout efetuado com sucesso!\n\n")
                        input("Pressione Enter para voltar ao menu inicial . . .")
                        print("-" * 50)
                        break

                    if(escolhadri == '1'):
                        cadastro_de_caronas.cadastrar_caronas()
                        
                    elif(escolhadri == '2'):
                        listar.listarcaronas()
                                
                    elif(escolhadri == '3'):
                        perorig = input("Digite o local de origem: ").lower().strip()
                        perdest = input("digite o local de destino: ").lower().strip()
                        encontrar.encontrar_carona(perorig, perdest)

                    elif(escolhadri == '4'):
                        excluir.excluir_a_carona()
    
                    elif(escolhadri == '5'):
                        listagem_particular.listagem_de_carona_particular()
                    
                    elif(escolhadri == '6'):
                        for dri in drivers: 
                            relatorio_caronas_mostrar(dri['email'])
                            relatorio_caronas_salvar(dri['email'])
                            input("Pressione Enter para continuar...")

                    input("Pressione Enter para continuar...")


    if(escolha == "7"):
        print(usuarios)
    if(escolha == "8"):
        print(drivers)
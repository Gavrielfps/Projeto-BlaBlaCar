from usuarios.motoristas.registro_e_validacao_email_motorista import drivers
import os

def login_driver(email, senha):
    encontradodri = False
    motoristalogado = None
    loginon = False
    menuon = False

    for dri in drivers:
        if(email == dri['email'] and senha == dri['senha'] and dri['tipo'] == "motorista"):
            encontradodri = True
            loginon = True
            print("-" * 50)
            print("Login efetuado. . .\n")
            print(f"Usuário: {dri['nome']} efetuou o login com sucesso!\n")
            print("Bem-Vindo(a)")
            print("-" * 50)
            menuon = True
            return dri
    
    if(not encontradodri):
        print("Usuário não existe!\n\n")
        os.system('cls' if os.name == 'nt' else 'clear')
    return None
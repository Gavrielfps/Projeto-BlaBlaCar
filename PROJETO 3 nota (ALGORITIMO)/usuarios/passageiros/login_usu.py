from usuarios.passageiros.registro_e_validacao_email import usuarios
import os

def login_do_usuario(email, senha):
    loging = False
    encontradousu = False
    menuon = False
    for usu in usuarios:
        if(email == usu['email'] and senha == usu['senha'] and usu['tipo'] == "passageiro"):
                encontradousu = True
                loging = True
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-" * 50)
                print("Login efetuado. . .\n")
                print(f"Usuário: {usu['nome']} efetuou o login com sucesso!\n")
                print(f"Bem-Vindo(a)")
                print("-" * 50)
                menuon = True
                return usu
    if(not encontradousu):
        print("Usuário não existe!\n\n")
    return None
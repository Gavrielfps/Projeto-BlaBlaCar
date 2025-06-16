caminho_do_usuarios = "usuarios\\passageiros\\usuarios.txt"
import os

usuarios = [{
             "nome": "Yasmin",
             "email": "yasmin@gmail.com",
             "senha": "2",
             "telefone": "(83)9999999999",
             "endereco": "Rua: ALEAROTIO222",
             "tipo": "passageiro",
},]

def salvar_passageiro_em_arquivos(nome, email, senha, telefone='', endereco='',):
    try:
      os.makedirs(os.path.dirname(caminho_do_usuarios), exist_ok=True)
      with open(caminho_do_usuarios, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome},{email},{senha},{telefone},{endereco},\n")
        print(f"Usuário {nome} salvo no arquivo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar usuário: {e}")

def email_invalido(email):
  if("@" not in email or ".com" not in email):
    print("O email inserido é inválido. Digite usando '@' e '.com' para conseguir se registrar e prosseguir!")
    return True

  return False
        
def cadastro_do_usuario_final(nome, email, senha, telefone, endereco):
    global usuarios

    emailexiste = False
    for usu in usuarios:
        if(email == usu['email'].lower()):
            print("O email já está cadastrado! Tente usar outro.\n")
            emailexiste = True
            return

    if(not emailexiste):
        novo_usuario = {
            'nome': nome,
            'email': email,
            'senha': senha,
            'telefone': telefone,
            'endereco': endereco,
            'tipo': 'passageiro'
        }
        usuarios.append(novo_usuario)
        salvar_passageiro_em_arquivos(nome, email.lower(), senha, telefone, endereco)
        print("Usuário cadastrado com sucesso!\n") 
        print(f"Dados do usuário: {nome}, {email}")
        input("Clique no Enter para continuar . . .")

def importar_arquivo_dos_passageiros():
  try:
      with open(caminho_do_usuarios, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            if(len(dados) >= 3):
              nome = dados[0]
              email = dados[1]
              senha =  dados[2]
              telefone = dados[3] if(len(dados) > 3) else ""
              endereco = dados[4] if(len(dados) > 4) else ""
            if(not any(email.lower() == usu['email'].lower() for usu in usuarios)):
                    usuarios.append({
                        'nome': nome,
                        'email': email,
                        'senha': senha,
                        'telefone': telefone,
                        'endereco': endereco,
                        'tipo': 'passageiro'
                    })
  except FileNotFoundError:
    print("Arquivo usuarios.txt não encontrado. Será criado quando o primeiro usuário for cadastrado.")
  except Exception as e:
    print(f"Erro ao importar usuários: {e}")
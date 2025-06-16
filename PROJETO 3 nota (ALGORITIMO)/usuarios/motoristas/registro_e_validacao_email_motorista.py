caminho_motorista = "usuarios\\motoristas\\motoristas.txt"
import os

drivers = [{"nome": "Gabriel", "email": "gabriel@gmail.com", "senha": "1", "telefone": "(83)8888888888", "endereco": "Rua: 999", "veiculo": "FIAT UNO", "placa": "zyt-431", "tipo": "motorista",},
           {"nome": "Lucas", "email": "lucas@gmail.com", "senha": "7", "telefone": "(83)7777777777", "endereco": "Rua: BR201", "veiculo": "SKYLINE", "placa": "SKE-223", "tipo": "motorista",},
          ]

def salvar_motoristas_em_arquivos(nome, email, senha, telefone, endereco, veiculo, placa):
  os.makedirs(os.path.dirname(caminho_motorista), exist_ok=True)
  with open(caminho_motorista, 'a', encoding='utf-8') as arquivo:
    arquivo.write(f"{nome},{email},{senha},{telefone},{endereco},{veiculo},{placa},\n")

def email_invalido_dri_e_cadastro_final(nome, email, senha, telefone, endereco, veiculo, placa):
    if("@" not in email or ".com" not in email):
        print("O email inserido é inválido. Digite usando '@' e '.com' para conseguir se registrar e prosseguir!")
        return False
    else:
        drivers.append({'nome':nome, 'email':email, 'senha':senha, 'telefone': telefone, 'endereco': endereco, 'veiculo': veiculo, 'placa': placa, 'tipo': 'motorista', "avaliacao": "[]",},)
        salvar_motoristas_em_arquivos(nome,email,senha)
        print("Usuário cadastrado com sucesso!\n") 
        print(f"Dados do usuário: {nome}, {email}")
        input("Clique no Enter para continuar . . .")
        return True

def email_igual_dri(email):
    while True:
        for dri in drivers:
            if(email == dri['email'].lower()):
                print("O email já está cadastrado! Tente usar outro.\n")
                return True

def importar_arquivo_dos_motoristas():
  try:
      os.makedirs(os.path.dirname(caminho_motorista), exist_ok=True)
      with open(caminho_motorista, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
          dados = linha.strip().split(',')
          if(len(dados) >= 3):
            nome = dados[0]
            email = dados[1]
            senha = dados[2]
          if(not any(email.lower() == dri['email'].lower() for dri in drivers)):
                    drivers.append({
                        'nome': nome,
                        'email': email,
                        'senha': senha,
                        'telefone': "",
                        'endereco': "",
                        'veiculo': "",
                        'placa': "",
                        'tipo': 'motorista',
                        'avaliacao': "[]"
                    })
  except FileNotFoundError:
    print("Arquivo motoristas.txt não encontrado. Será criado quando o primeiro motorista for cadastrado.")
  except Exception as e:
    print(f"Erro ao importar motoristas: {e}")

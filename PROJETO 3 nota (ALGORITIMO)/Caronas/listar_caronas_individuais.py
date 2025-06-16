from Caronas.cadastro_caronas import caronas
from usuarios.motoristas.registro_e_validacao_email_motorista import drivers


def listagem_de_carona_particular():
        encontradodri = True
        if(not encontradodri):
            print("Você precisa estar logado como motorista para ver suas caronas.\n")
        else:
            caronaencontrada = False
            for dri in drivers:
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
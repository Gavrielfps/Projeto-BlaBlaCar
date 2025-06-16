from Caronas.cadastro_caronas import caronas
from usuarios.motoristas.registro_e_validacao_email_motorista import drivers

def mostrar_detalhes_da_carona(emailmotorista5, datacarona5):
     for d in drivers:
        if(emailmotorista5 == d['email']):
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
                    return True
        if(not emailmotorista5):
            print("O email do motorista está incorreto!\n")
        elif(not datacarona5):
            print("A data digitada n corresponde com nenhuma das caronas disponíveis!\n")
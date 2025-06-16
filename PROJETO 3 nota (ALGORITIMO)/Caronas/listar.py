from Caronas.cadastro_caronas import caronas

def listarcaronas():
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
from Caronas.cadastro_caronas import caronas

def encontrar_carona(perorig, perdest):
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
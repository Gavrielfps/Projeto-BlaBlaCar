from Caronas.cadastro_caronas import caronas
import os

def mostrar_relatorio(email_motorista):
    total_geral = 0
    tem_caronas = False

    print("\n=== Relatorio de Caronas ===\n")

    for carona in caronas:
        if(carona['emailmotorista'] == email_motorista):
            tem_caronas = True
            vagas_ocupadas = int(carona['quantidadedevagas']) - len(carona['reserva'])
            total_carona = vagas_ocupadas * float(carona['valorporvaga'])
            total_geral += total_carona
            print("---------------------")
            print(f"Origem: {carona['localdeorigem']}")
            print(f"Destino: {carona['destino']}")
            print(f"Data: {carona['data']} - Horário: {carona['horario']}")
            print(f"Valor por vaga: R${float(carona['valorporvaga']):.2f}")
            print(f"Vagas restantes: {carona['quantidadedevagas']}")
            print(f"Total: R${total_carona:.2f}")
            print("---------------------")
    if(not tem_caronas):
        print("Não há caronas cadastradas")
    else:
        print(f"Total Geral: R${total_geral:.2f}")
    return tem_caronas

def salvar_relatorio(email_motorista):
    total_geral = 0
    if(not mostrar_relatorio(email_motorista)):
        return
    pergunta = input("\nDeseja salvar o relatório? (S/N): ").upper()
    if(pergunta == 'S'):
        os.makedirs("usuarios/motoristas/dados", exist_ok=True)
        caminho = (f"usuarios/motoristas/dados/relatorio_{email_motorista}.txt")
        try:
            with open(f"usuarios/motoristas/dados/relatorio_{email_motorista}.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("=== RELATORIO DE CARONAS ===\n\n")
                for carona in caronas:
                    if(carona['emailmotorista'] == email_motorista):
                        vagas_ocupadas = int(carona['quantidadedevagas']) - len(carona['reserva'])
                        total_carona = vagas_ocupadas * float(carona['valorporvaga'])
                        arquivo.write("---------------------")
                        arquivo.write(f"Origem: {carona['localdeorigem']}\n")
                        arquivo.write(f"Destino: {carona['destino']}\n")
                        arquivo.write(f"Data: {carona['data']} - Horário: {carona['horario']}\n")
                        arquivo.write(f"Valor por vaga: R${float(carona['valorporvaga']):.2f}\n")
                        arquivo.write(f"Vagas restantes: {carona['quantidadedevagas']}\n")
                        arquivo.write(f"Total: R${total_carona:.2f}\n")
                        arquivo.write("---------------------")
                arquivo.write(f"Total Geral: R${total_geral:.2f}\n")
            print("Relatório salvo em 'relatorio_caronas.txt'")
        except:
            print("Erro ao salvar o relatório")
    else:
        print("Você não salvou o Relatório . . . Voltando ao menu de motorista . . .")
        

        
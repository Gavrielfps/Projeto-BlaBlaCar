from Caronas.cadastro_caronas import caronas

def excluir_a_carona(c2):
    datacaronadriexc = input("Digite a data da carona desejada: ")
    desicion = input("Você deseja mesmo excluir a sua carona? (S / N): ").upper()
    if(desicion == "S"):
        for c2 in caronas:
            if(datacaronadriexc == c2["data"]):
                caronas.remove(c2)
                print("Carona excluida com sucesso!\n")
            else:
                print("Você não excluiu sua carona!")
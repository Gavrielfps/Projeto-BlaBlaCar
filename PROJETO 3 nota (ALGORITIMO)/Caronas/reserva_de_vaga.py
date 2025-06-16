from usuarios.motoristas.registro_e_validacao_email_motorista import drivers
from Caronas.cadastro_caronas import caronas
from usuarios.passageiros.registro_e_validacao_email import usuarios

def reservar_carona(emailmotorista3, datacarona3, confirmacaores3):
        for dri in drivers:
            if(emailmotorista3 == dri['email']):
                for d in caronas:
                    if(d["data"] == datacarona3 and d["emailmotorista"] == emailmotorista3):
                        if(confirmacaores3 == 'S'):
                            if(d["data"] == datacarona3 and d["emailmotorista"] == emailmotorista3):
                                if(int(d["quantidadedevagas"]) > 0):
                                    if(usuarios["nome"] not in d["reserva"]):
                                        d["reserva"].append(usuarios["nome"])
                                        d["quantidadedevagas"] = str(int(d["quantidadedevagas"]) - 1)
                                        print("Carona reservada com sucesso!\n")
                                    else:
                                        print("Você já reservou essa carona.\n")
                                else:
                                    print("Não há mais vagas disponíveis.\n")
                            else:
                                print("Reserva de Carona Cancelada com Sucesso!")
                                break
                            break
            if(not emailmotorista3):
                print("O email do motorista não existe dentro da aplicação! Tente usar um válido dentro das caronas disponíveis!\n")
            if(not datacarona3):
                print("Não existe nenhuma carona desse motorista com esta data!\n")
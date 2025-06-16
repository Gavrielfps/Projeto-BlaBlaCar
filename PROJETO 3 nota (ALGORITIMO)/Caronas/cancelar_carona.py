from Caronas.cadastro_caronas import caronas
from usuarios.motoristas.registro_e_validacao_email_motorista import drivers
from usuarios.passageiros.registro_e_validacao_email import usuarios

def cancelar_carona(emailmotorista4, datacarona4, confirmacaores4):
    for dri in drivers:
        if(emailmotorista4 == dri['email']):
            for c4 in caronas:
                if(datacarona4 == c4["data"] and c4['emailmotorista'] == dri["email"]):
                    if(confirmacaores4 == 'S'):
                        if(int(c4["quantidadedevagas"]) > 0):
                            c4["quantidadedevagas"] = int(c4["quantidadedevagas"]) + 1
                            if(usuarios["nome"] in c4["reserva"]):
                                c4["reserva"].remove(usuarios["nome"])
                                print("Carona cancelada com sucesso!\n")
                            else:
                                print("Não há caronas para serem canceladas!\n")
                        else:
                            if(usuarios["nome"] in c4["reserva"]):
                                c4["quantidadedevagas"] = int(c4["quantidadedevagas"]) + 1
                                c4["reserva"].remove(usuarios["nome"])
                                print("Carona cancelada com sucesso!\n")
                            else:
                                print("Não há caronas para serem canceladas!\n")
                    else:
                        print("Você não cancelou a vaga!\n")
                        break
                    break
                if(not datacarona4):
                    print("Não existe nenhuma carona desse motorista com essa data!\n")
                    return False
                if(not emailmotorista4):
                    print("O email do motorista não existe dentro da aplicação! Tente usar um valido dentro das caronas disponíveis!\n")
                    return False
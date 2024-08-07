from Função.Exception.Exception import ExceptionSimNao
def dadosSala(sala):

    while True:
        while True:
            print(f"\nDados da Sala {sala}\n")
            try:
                minTemp = int(input("Digite a temperatura mínima da sala: "))
                maxTemp = int(input("Digite a temperatura máxima da sala: "))
                setpointTemp = int(input("Digite o setpoint de temperatura da sala: "))
                minUmid = int(input("Digite a umidade mínimo da sala: "))
                maxUmid = int(input("Digite a umimdade máxima da sala: "))
                setpointUmid = int(input("Digite o setpoint de umidade da sala: "))

                break

            except:
                print("\nDigite apenas números!!!\n")
        print(f"\n======================\n"
              f"Dados da Sala {sala}\n"
              f"======================\n"
              f"Temperatura Mínima: {minTemp}\n"
              f"Temperatura Máxima: {maxTemp}\n"
              f"Setpoint Temperatura: {setpointTemp}\n"
              f"Umidade Mínima: {minUmid}\n"
              f"Umidade Máxima: {maxUmid}\n"
              f"Setpoint Umidade: {setpointUmid}\n")

        validacao = ExceptionSimNao("Os dados estão corretos:\n"
                                     "[1] - Sim\n"
                                     "[2] - Não\n")

        if validacao == 1:
            break


    dados = {
        "MinTemp":minTemp,
        "MaxTemp":maxTemp,
        "SetpointTemp": setpointTemp,
        "MinUmid": minUmid,
        "MaxUmid": maxUmid,
        "SetpointUmid": setpointUmid
    }


    return dados


def dadosSala(sala):

    while True:
        dados = []

        minTemp = int(input("Digite a temperatura mínima da sala: "))
        maxTemp = int(input("Digite a temperatura máxima da sala: "))
        setpointTemp = int(input("Digite o setpoint de temperatura da sala: "))
        minUmid = int(input("Digite a umidade mínimo da sala: "))
        maxUmid = int(input("Digite a umimdade máxima da sala: "))
        setpointUmid = int(input("Digite o setpont de umidade da sala: "))

        print(f"\n======================\n"
              f"Dados da Sala {'Exame' if sala else 'Técnica'}\n"
              f"======================\n"
              f"Temperatura Mínima: {minTemp}\n"
              f"Temperatura Máxima: {maxTemp}\n"
              f"Setpoint Temperatura: {setpointTemp}\n"
              f"Umidade Mínima: {minUmid}\n"
              f"Umidade Máxima: {maxUmid}\n"
              f"Setpoint Umidade: {setpointUmid}\n")

        validacao = int(input("Os valores estão corretos?\n"
                              "[1] - Sim\n"
                              "[2] - Não\n"))

        while validacao <= 0 or validacao >= 3:
            print("Valor Incorreto!!!\n")
            validacao = int(input("Os valores estão corretos?\n"
                                  "[1] - Sim\n"
                                  "[2] - Não\n"))
            if validacao == 1 or validacao == 2:
                break

        if validacao == 1:
            break

    dados.append(minTemp)
    dados.append(maxTemp)
    dados.append(setpointTemp)
    dados.append(minUmid)
    dados.append(maxUmid)
    dados.append(setpointUmid)

    return dados


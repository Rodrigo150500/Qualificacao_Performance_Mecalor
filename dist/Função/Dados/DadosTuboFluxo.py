def dadosTuboFluxo():
    while True:

        minTemp = int(input("Digite a temperatura mínima: "))
        maxTemp = int(input("Digite a temperatura máxima: "))
        setpointTemp = int(input("Digite o setpoint da temperatura: "))
        minVazao = int(input("Digite a vazão mínima: "))
        maxVazao = int(input("Digite a vazão máxima: "))
        setpointVazao = int(input("Digite o setpoint da vazão: "))

        print(f"\n======================\n"
              f"Dados Tubo de Fluxo\n"
              f"======================\n"
              f"Temperatura Mínima: {minTemp}\n"
              f"Temperatura Máxima: {maxTemp}\n"
              f"Setpoint Temperatura: {setpointTemp}\n"
              f"Vazão Mínima: {minVazao}\n"
              f"Vazão Máxima: {maxVazao}\n"
              f"Setpoint Vazão: {setpointVazao}\n")

        validacao = int(input("Os valores estão corretos?\n"
                              "[1] - Sim\n"
                              "[2] - Não\n"))

        while validacao <= 0 or validacao >= 3:
            print("Valor Incorreto!!!\n")
            validacao = int(input("Os valores estão corretos?\n"
                                  "[1] - Sim\n"
                                  "[2] - Não\n"))

            if (validacao == 1 or validacao == 2):
                break

        if (validacao == 1):
            break


    dados = {
        "MinTemp":minTemp,
        "MaxTemp": maxTemp,
        "SetpointTemp": setpointTemp,
        "MinVazao":minVazao,
        "MaxVazao": maxVazao,
        "SetpointVazao":setpointVazao
    }

    return dados


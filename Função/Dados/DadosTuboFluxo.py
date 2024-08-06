from Função.Exception.Exception import ExceptionSimNao

def dadosTuboFluxo():
    while True:
        while True:
            try:
                minTemp = int(input("Digite a temperatura mínima: "))
                maxTemp = int(input("Digite a temperatura máxima: "))
                setpointTemp = int(input("Digite o setpoint da temperatura: "))
                minVazao = int(input("Digite a vazão mínima: "))
                maxVazao = int(input("Digite a vazão máxima: "))
                setpointVazao = int(input("Digite o setpoint da vazão: "))
                break
            except:
                print("\nDigite apenas números!!!\n")
        print(f"\n======================\n"
              f"Dados Tubo de Fluxo\n"
              f"======================\n"
              f"Temperatura Mínima: {minTemp}\n"
              f"Temperatura Máxima: {maxTemp}\n"
              f"Setpoint Temperatura: {setpointTemp}\n"
              f"Vazão Mínima: {minVazao}\n"
              f"Vazão Máxima: {maxVazao}\n"
              f"Setpoint Vazão: {setpointVazao}\n")

        validacao = ExceptionSimNao("Os dados estão corretos:\n"
                                     "[1] - Sim\n"
                                     "[2] - Não\n")

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


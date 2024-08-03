def dadosEquipamento():
    while True:
        dados = []

        equipamento = input("Digite o nome do equipamento: ").upper()
        fabricante = input("Digite o nome do fabricante: ").upper()
        modelo = input("Digite o nome do modelo: ").upper()

        print(f"\n======================\n"
              f"Dados do Equipamento\n"
              f"======================\n"
              f"Equipamento: {equipamento}\n"
              f"Fabricante: {fabricante}\n"
              f"Modelo: {modelo}\n")

        validacao = int(input("Os valores estão corretos?\n"
                              "[1] - Sim\n"
                              "[2] - Não\n "))

        while validacao <= 0 or validacao >= 3:
            print("Valor Incorreto!!!")
            validacao = int(input("Os valores estão corretos?\n"
                                  "[1] - Sim\n"
                                  "[2] - Não\n "))
            if (validacao == 1 or validacao == 2):
                break

        if(validacao == 1):
            break

    dados.append(equipamento)
    dados.append(fabricante)
    dados.append(modelo)

    return dados


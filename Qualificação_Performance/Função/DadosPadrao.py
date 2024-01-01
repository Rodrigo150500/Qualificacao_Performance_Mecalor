def dadosPadrao():
    while True:
        dados = []
        nome = input("Digite o nome do coordenador: ").strip()
        sigla = input("Digite a sigla: ").strip()
        cliente = input("Digite o nome do cliente: ").strip()
        OS = input("Digite o nome da OS: ").strip()
        dataColeta = input("Digite a data da coleta dos Logs: ").strip()

        print(f"\nNome: {nome}\n"
              f"Sigla: {sigla}\n"
              f"Cliente: {cliente}\n"
              f"OS: {OS}\n"
              f"Data da Coleta: {dataColeta}\n")

        validacao = int(input("Os dados estão corretos: \n"
                              "[1] - Sim\n"
                              "[2] - Não\n"))
        while validacao <= 0 or validacao >= 3:
            print("Valor Incorreto!!!\n")
            validacao = int(input("Os dados estão corretos: \n"
                                  "[1] - Sim\n"
                                  "[2] - Não\n"))
            if validacao == 1 or validacao == 2:
                break

        if validacao == 1:
            break
    dados.append(nome)
    dados.append(sigla)
    dados.append(cliente)
    dados.append(OS)
    dados.append(dataColeta)

    return dados



from Função.Exception.Exception import ExceptionSimNao

def dadosPadrao():
    while True:
        nome = input("Digite o nome do coordenador: ").upper()
        sigla = input("Digite a sigla: ").upper()
        cliente = input("Digite o nome do cliente: ").upper()
        OS = input("Digite o nome da OS: ").upper()
        dataColeta = input("Digite a data da coleta dos Logs: ").upper()

        print(f"\n==============\n"
              f"Dados Gerais \n"
              f"==============\n"
              f"Nome: {nome}\n"
              f"Sigla: {sigla}\n"
              f"Cliente: {cliente}\n"
              f"OS: {OS}\n"
              f"Data da Coleta: {dataColeta}\n")

        validacao = ExceptionSimNao("Os dados estão corretos:\n"
                                     "[1] - Sim\n"
                                     "[2] - Não\n")
        if validacao == 1:
            break

    dados = {
        "Nome":nome,
        "Sigla": sigla,
        "Cliente":cliente,
        "OS": OS,
        "DataColeta": dataColeta
    }
    return dados

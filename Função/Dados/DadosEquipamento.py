from Função.Exception.Exception import ExceptionSimNao
def dadosEquipamento():
    while True:

        while True:
            fabricante = input("Digite o nome do fabricante: ").upper()
            modelo = input("Digite o nome do modelo: ").upper()

            if ((fabricante != "") and (modelo != "")):
                break
            else:
                print("\nPreencha todos os campos!!!\n")

        print(f"\n======================\n"
              f"Dados do Equipamento\n"
              f"======================\n"
              f"Fabricante: {fabricante}\n"
              f"Modelo: {modelo}\n")

        validacao = ExceptionSimNao("Os dados estão corretos:\n"
                                     "[1] - Sim\n"
                                     "[2] - Não\n")

        if(validacao == 1):
            break

    dados = {
        "Fabricante": fabricante,
        "Modelo": modelo
    }

    return dados


import os

listaLog = []
opcao = ['Sala Exames/Sala Técnica','Sala Exames','Sala Técnica','Sala Adicional','Tubo de Fluxo']
def verificarArquivos():

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Logs'))
    logs_directory = path.replace("\\", "/")
    
    arquivos = os.listdir(logs_directory)

    #Verificando se há arquivos na pasta GerarColunas
    if len(arquivos) < 1:
        print("Sem arquivos na pasta Logs\n")
        return False
    else:
        while True:
            for arquivo in arquivos:

                ###
                # A opção escolhida será de acordo com a sala sendo lida,
                # em alguns casos quando a leitura é apenas de uma sala
                # a coluna da sala técnica tem como preferência mesmo sendo uma sala de exames
                ###

                while True:
                    print(f'Que tipo de arquivo é {arquivo}?\n')
                    tipoArquivo = int(input(
                        '[1] - Sala Exames/Sala Técnica\n'
                        '[2] - Sala Exame   \n'
                        '[3] - Sala Técnica\n'
                        '[4] - Sala Adicional\n'
                        '[5] - Tubo de Fluxo\n'
                    ))
                    if tipoArquivo <= 0 or tipoArquivo >= 6:
                        print("Valor incorret, digite novamente!!!\n")
                    else:
                        temp = [tipoArquivo, arquivo, opcao[tipoArquivo-1]]
                        listaLog.append(temp)
                        break

            #Apresentando as respostas do usuario
            print("Conferindo os arquivos!\n")
            for arquivo in listaLog:
                print(f' {arquivo[1]} --> {opcao[arquivo[0]-1]} ')
            print("")

            validacao = int(input("Os arquivos estão corretos?\n"
                                  "[1] - Sim\n"
                                  "[2] - Não\n"))

            #Verificando se a resposta está dentro das opções
            while validacao <= 0 or validacao >= 3:
                print("Valores Incorretos!!!")
                validacao = int(input("Os arquivos estão corretos?\n"
                                      "[1] - Sim\n"
                                      "[2] - Não\n"))
            if(validacao == 1):
                break
            else:
                listaLog.clear()

    return listaLog
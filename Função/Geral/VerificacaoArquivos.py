from Função.Exception.Exception import ExceptionSimNao
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado
import os



listaLog = []
opcao = ['Sala Exames/Sala Técnica', 'Sala Exames', 'Sala Técnica', 'Sala Adicional', 'Tubo de Fluxo']

def verificarArquivos():
    caminho = os.path.join(acharCaminhoExecutado("Logs"))
    arquivos = os.listdir(caminho)


    # Verificando se há arquivos na pasta GerarColunas
    if len(arquivos) < 1:
        print("Sem arquivos na pasta Logs\n")
        input("Aperte ENTER para continuar...")
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

                    while True:
                        print(f'\nQue tipo de arquivo é {arquivo}?\n')
                        try:
                            tipoArquivo = int(input( "[1] - Sala Exames/Sala Técnica\n" \
                                                     "[2] - Sala Exame   \n" \
                                                     "[3] - Sala Técnica\n" \
                                                     "[4] - Sala Adicional\n" \
                                                     "[5] - Tubo de Fluxo\n"))

                            if(tipoArquivo in [1, 2, 3, 4, 5]):
                                break
                            else:
                                print("\nDigite Valores Válidos!!!\n")
                        except:
                            print("\nDigite Valores Válidos!!!\n")

                    temp = {
                        "Input": tipoArquivo,
                        "Log": arquivo,
                        "Opcao": opcao[tipoArquivo - 1],
                        "Diretorio": os.path.join(acharCaminhoExecutado('Logs'), arquivo)
                    }
                    listaLog.append(temp)

                    break


            # Apresentando as respostas do usuario
            print("Conferindo os arquivos!\n")
            for item in listaLog:
                print(f' {item["Log"]} --> {item["Opcao"]} ')
            print("")

            validacao = ExceptionSimNao("Os dados estão corretos: \n"
                                        "[1] - Sim\n"
                                        "[2] - Não\n")

            if validacao == 1:
                break
            else:
                listaLog.clear()


    listaLog.append({
        "DiretorioLogRaiz": caminho
    })

    return listaLog



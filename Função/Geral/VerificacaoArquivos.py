import os
import sys
listaLog = []
opcao = ['Sala Exames/Sala Técnica', 'Sala Exames', 'Sala Técnica', 'Sala Adicional', 'Tubo de Fluxo']


def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)


def verificarArquivos():

    arquivos = os.listdir(os.path.join(get_executable_path(), "Logs"))

    # Verificando se há arquivos na pasta GerarColunas
    if len(arquivos) < 1:
        print("Sem arquivos na pasta Logs\n")
        return False
    else:
        while True:
            for arquivo in arquivos:
                print(f'Arquivo {arquivo}')
                print(f'juntando {os.path.join(get_executable_path(), "Logs", arquivo)}')


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

                        temp = {
                            "Input": tipoArquivo,
                            "Log": arquivo,
                            "Opcao": opcao[tipoArquivo - 1],
                            "Diretorio": os.path.join(get_executable_path(),'Logs',arquivo)
                        }
                        listaLog.append(temp)
                        break

            # Apresentando as respostas do usuario
            print("Conferindo os arquivos!\n")
            for item in listaLog:
                print(f' {item["Log"]} --> {item["Opcao"]} ')
            print("")

            validacao = int(input("Os arquivos estão corretos?\n"
                                  "[1] - Sim\n"
                                  "[2] - Não\n"))

            # Verificando se a resposta está dentro das opções
            while validacao <= 0 or validacao >= 3:
                print("Valores Incorretos!!!")
                validacao = int(input("Os arquivos estão corretos?\n"
                                      "[1] - Sim\n"
                                      "[2] - Não\n"))
            if (validacao == 1):
                break
            else:
                listaLog.clear()
    listaLog.append({
        "DiretorioLogRaiz": os.path.join(get_executable_path(), "Logs")
    })
    return listaLog




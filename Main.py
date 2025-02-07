from Função.Geral.VerificacaoArquivos \
    import verificarArquivos
from Caminhos.CaminhoCompletoPadrao import caminhoCompletoPadrao
from Caminhos.CaminhoResumidoPadrao import caminhoResumidoPadrao


print('='*20)
print("INICIANDO PROGRAMA")
print('='*20)

#Verificando os arquivos
listaLog = verificarArquivos()

#Definino caminho e seu tipo
#Sendo caminho:
#1 - Completo 2 - Resumido
#Tipo Caminho
#1 - Padrão - 2 Personalizado
###
if listaLog != False:
    print("Caminho Completo Padrão\n")

    caminhoCompletoPadrao(listaLog)


'''
    while True:
        #Definindo o caminho se é COMPLETO ou RESUMI1DO
        caminho = int(input("Digite se o caminho que o programa fará:\n"
                              "[1] - Completo\n"
                              "[2] - Resumido\n"))
        while caminho <= 0 or caminho >= 3:
            print("Valor Incorreto!!!\n")
            caminho = int(input("Digite se o programa será feito:\n"
                                 "[1] - Completo\n"
                                 "[2] - Resumido\n"))
            if caminho == 1 or caminho == 2:
                break

        #Definindo o tipo de caminho se é PADRÃO ou PERSONALIZADO
        tipoCaminho = int(input("Digite qual tipo de caminho o programa fará: \n"
                                "[1] - Padrão\n"
                                "[2] - Personalizado\n"))
        while tipoCaminho <= 0 or tipoCaminho >= 3:
            print("Valor Incorreto\n")
            tipoCaminho = int(input("Digite qual tipo de caminho o programa fará: \n"
                                    "[1] - Padrão\n"
                                    "[2] - Personalizado\n"))
        if caminho == 1:
            print("O caminho será Completo\n")

        else:
            print("O caminho será Resumido\n")

        if tipoCaminho == 1:
            print("O tipo do caminho será Padrão\n")
        else:
            print("O tipo do caminho será Personalizado\n")

        validacaoCaminho = int(input("Os valores estão corretos: \n"
                                     "[1] - Sim\n"
                                     "[2] - Não\n"))
        if(validacaoCaminho == 1):
            break

    #Caminho Completo Padrão
    if(caminho == 1 and tipoCaminho == 1):
        print("Caminho Completo Padrão\n")

        caminhoCompletoPadrao(listaLog)

    #Caminho Completo Personalizado
    elif (caminho == 1 and tipoCaminho == 2):
        print("Caminho Completo Personalizado\n")
        pass
    #Caminho Resumido Padrão
    elif (caminho == 2 and tipoCaminho == 1):
        print("Caminho Resumido Padrão\n")
        pass
    #Caminho Resumido Personalizado
    elif (caminho == 2 and tipoCaminho == 2):
        print("Caminho Resumido Personalizado\n")
        pass
'''
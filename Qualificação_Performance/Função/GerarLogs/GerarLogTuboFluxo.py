import os

def verificarLogTuboFluxo(tuboFluxo, listaLog):
    #Fazer uma condição para ler apenas o log de exames conforme foi selecionado
    logDiretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Logs'))
    logs = os.listdir(logDiretorio)


    for opcao in listaLog:
        for log in logs:
            if(opcao[1] == log and opcao[0] == 5):

                diretorio = os.path.join(logDiretorio,log)
                gerarLog(tuboFluxo, diretorio)

def gerarLog(tuboFluxo, log):
    pass
import os

def verificarLog(n, listaLog):
    #Fazer uma condição para ler apenas o log selecionado
    logDiretorioPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Logs')) 
    logDiretorio = logDiretorioPath.replace("\\", "/")
    logs = os.listdir(logDiretorio)

    for opcao in listaLog:
        for log in logs:
            if(opcao[1] == log and opcao[0] == n):
                diretorio = os.path.join(logDiretorio,log)
                return diretorio,log, opcao[2]


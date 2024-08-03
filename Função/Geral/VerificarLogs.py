import os
import sys
def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)
def verificarLog(n, listaLog):
    #Fazer uma condição para ler apenas o log selecionado
    logDiretorio = os.path.join(get_executable_path(), 'Logs').replace("\\","/")
    logs = os.listdir(logDiretorio)

    for opcao in listaLog:
        for log in logs:
            if(opcao[1] == log and opcao[0] == n):
                diretorio = os.path.join(logDiretorio,log)
                return diretorio,log, opcao[2]


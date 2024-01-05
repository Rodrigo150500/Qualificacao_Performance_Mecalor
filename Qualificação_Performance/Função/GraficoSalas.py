import os
import pandas as pd

"""
    '[1] - Sala Exames/Técnica\n'
    '[2] - Sala Exame   \n'
    '[3] - Sala Técnica\n'
    '[4] - Sala Adicional\n'
    '[5] - Tubo de Fluxo\n'
"""

def graficoSalas(salaExames, salaTecnica, listaLog):
    #Fazer uma condição para ler apenas o log de exames conforme foi selecionado

    logDiretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logs'))
    logs = os.listdir(logDiretorio)


    for opcao in listaLog:
        for log in logs:
            if(opcao[1] == log and opcao[0] == 1):
                diretorio = os.path.join(logDiretorio,log)
                gerarGrafico(salaExames, salaTecnica, diretorio)
def gerarGrafico(salaExames, salaTecnica, log):
    dados = pd.read_csv(log, sep=',')
    dados["Data2"] = str(dados["Data"][0:7])
    print(dados.tail())

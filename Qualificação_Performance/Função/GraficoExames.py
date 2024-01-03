import os
import pandas as pd

"""
    '[1] - Sala Exames/Técnica\n'
    '[2] - Sala Exame   \n'
    '[3] - Sala Técnica\n'
    '[4] - Sala Adicional\n'
    '[5] - Tubo de Fluxo\n'
"""

def graficoExames(minTemp, maxTemp, setpointTemp, minUmid, maxUmid, setpointUmid, listaLog):
    #Fazer uma condição para ler apenas o log de exames conforme foi selecionado

    logs_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logs'))



    primeiro_arquivo = os.listdir(logs_directory)[0]
    caminho_arquivo = os.path.join(logs_directory, primeiro_arquivo)
    dados = pd.read_csv(caminho_arquivo)

    print(dados)
graficoExames(15,25,25,25,25,25,25)
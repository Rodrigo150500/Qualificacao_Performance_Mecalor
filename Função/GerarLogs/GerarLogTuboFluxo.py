import os
import pandas as pd
from Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora
from Função.GerarColunas.GerarColunaTuboFluxo import gerarColunaTuboFluxo

def gerarLogTuboFluxo(tuboFluxo, diretorio, nome):
    dados = pd.read_csv(diretorio, sep=',')

    # Gerando a coluna de data e hora
    dados = gerarColunaDataHora(dados)

    # Gerando a coluna do tubo de Fluxo
    dados = gerarColunaTuboFluxo(dados=dados, tuboFluxo=tuboFluxo)

    # Excluindo as colunas desnecessárias
    dados.drop(['TempRetAG (C/10)',
                'PresAlimAG (bar/10)',
                'PresRetAG (bar/10)',
                'VzGradCoil (l/min/10)',
                'VzGradPwr (l/min/10)',
                'VzComp (l/min/10)'
    ], axis=1, inplace=True)

    # Reorganizando as colunas
    dados = dados[['Data', 'Data2', 'Hora',
                   "Temp AlimAG Min (°C)",
                   "Temp AlimAG Max (°C)",
                   "Temp AlimAG (°C)",
                   "Vz AlimAG Min (l/min)",
                   "Vz AlimAG Max (l/min)",
                   "Vz AlimAG (l/min)",
                   ]]

    # Dividindo as colunas por 10
    dados["Temp AlimAG (°C)"] /= 10
    dados["Vz AlimAG (l/min)"] /= 10

    # Substituindo pontos por vírgulas nas colunas específicas
    colunas_substituir = ["Temp AlimAG (°C)", "Vz AlimAG (l/min)"]
    dados[colunas_substituir] = dados[colunas_substituir].astype(str).apply(lambda x: x.str.replace('.', ','))

    # Definindo o caminho para salvar o novo log atualizado
    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Resultado', "LogsAtualizados")).replace("\\", "/")
    nomeLog = os.path.join(caminho, nome).replace("\\", "/")

    dados.to_csv(nomeLog, index=False, sep=';', encoding="cp1252")


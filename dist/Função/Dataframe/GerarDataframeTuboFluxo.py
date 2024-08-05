import os
import pandas as pd
from Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora
import sys

def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)


def gerarDataframeTuboFluxo(tubofluxo, diretorio, nome, datas):
    logTubo = pd.read_csv(diretorio, sep=',')

    listaDataHora = gerarColunaDataHora(logTubo)

    leituraTemp = logTubo["TempAlimAG (C/10)"]/10
    leituraVazao = logTubo["VzAlimAG (l/min/10)"]/10

    dadosTubo = {
        "Data":listaDataHora[0],
        "Hora":listaDataHora[1],
        "TempAG Min (°C)" : tubofluxo.minTemp,
        "TempAG Max (°C)" : tubofluxo.maxTemp,
        "TempAG (°C)": leituraTemp,
        "Vazão Alim Min (l/min)": tubofluxo.minVazao,
        "Vazão Alim Max (l/min)": tubofluxo.maxVazao,
        "Vazão Alim (l/min)": leituraVazao
    }

    colunas = []
    for coluna in dadosTubo:
        if coluna != "Data" and coluna != "Hora":
            colunas.append(coluna)
    dataFrameTubo = pd.DataFrame(data=dadosTubo)
    dataFrameTubo = dataFrameTubo[dataFrameTubo["Data"].isin(datas)].reset_index(drop=True)

    salvarDir = os.path.normpath(os.path.join(get_executable_path(),"../../Resultado/LogsAtualizados",nome))

    dataFrameTubo.to_csv(salvarDir,index=False, sep=',', encoding="cp1252")

    return dataFrameTubo, colunas

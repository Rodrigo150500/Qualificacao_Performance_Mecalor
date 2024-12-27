import os
import pandas as pd
from Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora
import sys
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado




def gerarDataframeTuboFluxo(tubofluxo, diretorio, nome, datas, arquivoTxt = False):

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

    if not arquivoTxt:
        dataFrameTubo = pd.DataFrame(data=dadosTubo)

        salvarDir = os.path.normpath(os.path.join(acharCaminhoExecutado("Resultado/LogsAtualizados"),nome))

        dataFrameTubo.to_csv(salvarDir,index=False, sep=',', encoding="cp1252")

        dataFrameTuboGrafico = dataFrameTubo[dataFrameTubo["Data"].isin(datas)].reset_index(drop=True)


        return dataFrameTubo, colunas, dataFrameTuboGrafico
    else:
        dataFrameTubo = pd.DataFrame(data=dadosTubo)
        salvarDir = os.path.normpath(os.path.join(acharCaminhoExecutado("Resultado/LogsAtualizados"),nome))
        
        colunas_substituir = ["TempAG (°C)", "Vazão Alim (l/min)"]
        dataFrameTubo[colunas_substituir] = dataFrameTubo[colunas_substituir].astype(str).apply(lambda x: x.str.replace('.', ','))

        dataFrameTubo.to_csv(salvarDir,index=False, sep=';', encoding="cp1252")

        dataFrameTuboGrafico = dataFrameTubo[dataFrameTubo["Data"].isin(datas)].reset_index(drop=True)

        return


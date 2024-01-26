import os
import pandas as pd
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora
import matplotlib.pyplot as plt
from collections import OrderedDict

def verificarDatas(listaDatas, sala):

    datas = []
    print(f"Quais datas farão parte do QP da {sala}:\n")
    for data in listaDatas:
        while True:
            res = int(input(f"Deseja incluir a data: {data}\n"
                            f"[1] - Sim\n"
                            f"[2] - Não\n"))
            if res <= 0 or res >= 3:
                print("Valores Incorretos")
            else:
                break
        if res == 1:
            datas.append(data)

    return datas


def gerarGrafico(dados, colunas, titulo):
    dataFrames = pd.DataFrame(dados)

    df = dataFrames.plot(
        kind='line',
        x='Hora',
        y=colunas,
        color=['red', 'blue'],
        title=titulo,
        figsize=(18, 8),
        linewidth=1
    )
    #Arrumando o eixo das Horas
    amostra_indices = range(0,len(dataFrames["Hora"]),300)
    amostra_rotulos = dataFrames["Hora"].iloc[amostra_indices]
    df.set_xticks(amostra_rotulos.index)
    df.set_xticklabels(amostra_rotulos, rotation=45, ha='right')

    df.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

    intervalo_y = range(0, int(max(dataFrames[colunas].max()) + 5), 5)
    df.set_yticks(intervalo_y)
    df.set_xlim(0)
    plt.show()


def graficoPreviewCCP(n,listaLog):
    logDiretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Logs'))
    logs = os.listdir(logDiretorio)

    for opcao in listaLog:
        for log in logs:
            if(opcao[1] == log and opcao[0] == n):
                logDiretorio = os.path.join(logDiretorio,log)

                if(n == 1):
                    logSalas = pd.read_csv(logDiretorio,sep=',')
                    dataHora = gerarColunaDataHora(logSalas)
                    data = dataHora[0]
                    hora = dataHora[1]
                    dados = {
                        "Data":data,
                        "Hora":hora,
                        "Temp Equip (°C)":logSalas["TempEquip1 (C/10)"]/10,
                        "Umid Equip (%)":logSalas["UmdEquip1 (UR/10)"]/10,
                        "Temp Exame (°C)":logSalas["TempExame1 (C/10)"]/10,
                        "Umid Exame (%)":logSalas["UmdExame1 (UR/10)"]/10
                    }
                    colunaTecnica = []
                    colunaExame = []

                    listaDatas = list(OrderedDict.fromkeys(data))
                    for coluna in dados:
                        if "Exame" in coluna:
                            colunaExame.append(coluna)
                        elif "Equip" in coluna:
                            colunaTecnica.append(coluna)


                    gerarGrafico(dados, colunaTecnica, "Sala Técnica")
                    gerarGrafico(dados, colunaExame, "Sala Exames")
                    datas = verificarDatas(listaDatas, "Sala Técnica/Exames")
                    return datas

                elif (n == 5):
                    logTubo = pd.read_csv(logDiretorio,sep=',')
                    dataHora = gerarColunaDataHora(logTubo)
                    data = dataHora[0]
                    hora = dataHora[1]
                    dados = {
                        "Data": data,
                        "Hora": hora,
                        "Temp AG (°C)":logTubo["TempAlimAG (C/10)"]/10,
                        "Vazão AG (l/min)":logTubo["VzAlimAG (l/min/10)"]/10
                    }
                    colunas = []
                    listaDatas = list(OrderedDict.fromkeys(data))
                    for coluna in dados:
                        if "AG" in coluna:
                            colunas.append(coluna)
                    titulo = "Tubo de Fluxo"
                    gerarGrafico(dados, colunas, titulo)
                    datas = verificarDatas(listaDatas, "Tubo de Fluxo")
                    return datas



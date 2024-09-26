import os
import pandas as pd

from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado
from Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora
from Função.Exception.Exception import ExceptionSimNao
import matplotlib.pyplot as plt
from collections import OrderedDict

def verificarDatas(listaDatas, sala):

    datas = []

    while True:
        print(f"\nQuais datas farão parte do QP da {sala}:\n")
        for data in listaDatas:

            res = ExceptionSimNao(f"Deseja incluir a data: {data}\n"
                                    f"[1] - Sim\n"
                                    f"[2] - Não\n")
            if res == 1:
                datas.append(data)

        if len(datas) < 1:
            print("Coloque pelo menos 1 data")
        else:
            break
    return datas


def gerarGrafico(dados, colunas, titulo, caminhoCompleto):
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



    total_pontos = len(dataFrames["Hora"])
    max_rótulos = 55  # Número máximo de rótulos que desejamos no eixo X

    # Calculando o intervalo de amostragem para rótulos de hora
    if total_pontos <= max_rótulos:
        intervalo_amostra = 1
    else:
        intervalo_amostra = total_pontos // max_rótulos


    #Arrumando o eixo das Horas
    amostra_indices = range(0,len(dataFrames["Hora"]),intervalo_amostra)
    amostra_rotulos = dataFrames["Hora"].iloc[amostra_indices]
    df.set_xticks(amostra_rotulos.index)
    df.set_xticklabels(amostra_rotulos, rotation=45, ha='right')

    df.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

    intervalo_y = range(0, int(max(dataFrames[colunas].max()) + 5), 5)
    df.set_yticks(intervalo_y)
    df.set_xlim(0)
    if(not caminhoCompleto):
        print('foto salva')
        plt.savefig(os.path.join(acharCaminhoExecutado('Resultado/FotosGrafico'),  f'{titulo}.png'),  bbox_inches='tight')

    plt.show()



def graficoPreview(listaLog, numeroOpcao, caminhoCompleto):

    #Diretorio dos logs
    logDiretorio = listaLog[-1]["DiretorioLogRaiz"]


    #Pegando os arquivos do diretório
    logs = os.listdir(logDiretorio)


    for item in listaLog:
        for log in logs:
            if(item["Log"] == log and item["Input"] == numeroOpcao):

                #Diretorio com o nome específico do log, e.g  c:../../logSala.txt
                logArquivo = os.path.join(logDiretorio,log)

                #Condição para Sala Exames/Técnica
                if(item["Opcao"] == 'Sala Exames/Sala Técnica'):
                    logSalas = pd.read_csv(logArquivo,sep=',')
                    data, hora = gerarColunaDataHora(logSalas)

                    dados = {
                        "Data":data,
                        "Hora":hora,
                        "Temp Equip (°C)":logSalas["TempEquip1 (C/10)"]/10,
                        "Umid Equip (%)":logSalas["UmdEquip1 (UR/10)"]/10,
                        "Temp Exame (°C)":logSalas["TempExame1 (C/10)"]/10,
                        "Umid Exame (%)":logSalas["UmdExame1 (UR/10)"]/10
                    }

                    #Colunas para separar os título que forem das salas técnicas e exames
                    colunaTecnica = []
                    colunaExame = []

                    #Ordenando as datas
                    listaDatas = list(OrderedDict.fromkeys(data))

                    #Separando o nome das colunas que forem pertinentes para Sala Técnica e Exames
                    for coluna in dados:
                        if "Exame" in coluna:
                            colunaExame.append(coluna)
                        elif "Equip" in coluna:
                            colunaTecnica.append(coluna)

                    #Mostrando as datas
                    datas = ''
                    print("="*40)
                    print(f"Datas para a Sala Técnica/Exames")
                    print("="*40)
                    for data in listaDatas:
                        datas += f"{data}, "
                    print(datas)

                    input("Essas são as datas, pressione ENTER para continuar...")


                    #Gerando o gráfico, os dados é o log processado porém filtrado pelo nome das colunas
                    gerarGrafico(dados, colunaTecnica, "Sala Técnica", caminhoCompleto=caminhoCompleto)
                    gerarGrafico(dados, colunaExame, "Sala Exames", caminhoCompleto = caminhoCompleto)

                    #Perguntando quais datas vão para o gráfico final
                    if (not caminhoCompleto):
                        return
                    datas = verificarDatas(listaDatas, "Sala Técnica/Exames")
                    return datas


                #Condição para Sala Exames ou Sala Adicional
                elif ((item["Opcao"] == "Sala Exames") or (item["Opcao"] == 'Sala Adicional')):
                    pass

                #Condição para Sala Técnica
                elif (item["Opcao"] == "Sala Técnica"):
                    pass

                #Condição para Tubo de Fluxo
                elif (item["Opcao"] == "Tubo de Fluxo"):
                    logTubo = pd.read_csv(logArquivo,sep=',')
                    data, hora = gerarColunaDataHora(logTubo)

                    dados = {
                        "Data": data,
                        "Hora": hora,
                        "Temp AG (°C)":logTubo["TempAlimAG (C/10)"]/10,
                        "Vazão AG (l/min)":logTubo["VzAlimAG (l/min/10)"]/10
                    }

                    #Colunas será para armazenar o título de cada coluna que for pertinente ao tubo de fluxo
                    colunas = []

                    #Pegando as datas
                    listaDatas = list(OrderedDict.fromkeys(data))
                    for coluna in dados:
                        if "AG" in coluna:
                            colunas.append(coluna)
                    titulo = "Tubo de Fluxo"

                    #Gerando gráfico pegando os dados do log processado e filtrando com a coluna pertinente ao tubo
                    # de fluxo
                    gerarGrafico(dados, colunas, titulo, caminhoCompleto=caminhoCompleto)

                    #Perguntando quais datas vão estar no gráfico final do tubo de fluxo
                    if(not caminhoCompleto):
                        return
                    datas = verificarDatas(listaDatas, "Tubo de Fluxo")
                    return datas



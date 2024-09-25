import os
import matplotlib.pyplot as plt
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado


def gerarGrafico(dataFrames, colunas, nomeImg, titulo):

    nome = nomeImg.split(".")[0] + ".png"


    caminhoSalvar = os.path.join(acharCaminhoExecutado('Resultado/FotosGrafico'), nome)


    dataframeArquivo = dataFrames.plot(
        kind='line',
        x = 'Hora',
        y = colunas,
        color = ['purple','purple','red','orange','orange','blue'],
        title=titulo,
        figsize = (18,8),
        linewidth = 1
    )



    total_pontos = len(dataFrames["Hora"])
    max_rótulos = 55  # Número máximo de rótulos que desejamos no eixo X

    # Calculando o intervalo de amostragem para rótulos de hora
    if total_pontos <= max_rótulos:
        intervalo_amostra = 1
    else:
        intervalo_amostra = total_pontos // max_rótulos


    #Arrumando o eixo das Horas
    amostra_indices = range(0,len(dataFrames["Hora"]), intervalo_amostra)
    amostra_rotulos = dataFrames["Hora"].iloc[amostra_indices]
    dataframeArquivo.set_xticks(amostra_rotulos.index)
    dataframeArquivo.set_xticklabels(amostra_rotulos, rotation=45, ha='right')

    #Deslocando a legenda para fora do gráfico
    dataframeArquivo.legend(bbox_to_anchor=(1.01, 1), loc='upper left')


    intervalo_y = range(0, int(max(dataFrames[colunas].max()) + 5), 5)
    dataframeArquivo.set_yticks(intervalo_y)
    dataframeArquivo.set_xlim(0)

    plt.savefig(caminhoSalvar, bbox_inches='tight')





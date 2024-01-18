import os
import matplotlib.pyplot as plt
import openpyxl
from openpyxl.drawing.image import Image
def gerarGrafico(dataFrames, colunas, nomeImg,titulo,posicao):
    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../Resultado/Qualificacao.xlsx'))
    nome = nomeImg.split(".")[0] + ".png"
    salvarImagem = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../Resultado/FotosGrafico", nome))

    dfTubo = dataFrames.plot(
        kind='line',
        x = 'Hora',
        y = colunas,
        color = ['red','red','blue','orange','orange','purple'],
        title=titulo,
        figsize = (18,8),
        linewidth = 1
    )

    #Arrumando o eixo das Horas
    amostra_indices = range(0,len(dataFrames["Hora"]),300)
    amostra_rotulos = dataFrames["Hora"].iloc[amostra_indices]
    dfTubo.set_xticks(amostra_rotulos.index)
    dfTubo.set_xticklabels(amostra_rotulos, rotation=45, ha='right')

    dfTubo.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

    intervalo_y = range(0, int(max(dataFrames[colunas].max()) + 5), 5)
    dfTubo.set_yticks(intervalo_y)
    dfTubo.set_xlim(0)

    plt.savefig(salvarImagem, bbox_inches='tight')

    workbook = openpyxl.load_workbook(caminho)

    abaGrafico = workbook["Grafico"]


    img = Image(salvarImagem)
    abaGrafico.add_image(img,posicao)

    workbook.save(caminho)





import os
import matplotlib.pyplot as plt
import sys
def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)
def gerarGrafico(dataFrames, colunas, nomeImg,titulo):
    nome = nomeImg.split(".")[0] + ".png"

    salvarImagem = os.path.normpath(os.path.join(get_executable_path(), "../../Resultado/FotosGrafico", nome))


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

    #Deslocando a legenda para fora do gráfico
    dfTubo.legend(bbox_to_anchor=(1.01, 1), loc='upper left')


    intervalo_y = range(0, int(max(dataFrames[colunas].max()) + 5), 5)
    dfTubo.set_yticks(intervalo_y)
    dfTubo.set_xlim(0)

    plt.savefig(salvarImagem, bbox_inches='tight')





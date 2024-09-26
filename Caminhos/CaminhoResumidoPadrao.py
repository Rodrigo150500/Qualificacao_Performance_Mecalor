from Função.Geral.LimparLogs import limparResultados
from Função.Grafico.GraficoPreview import graficoPreview

def caminhoResumidoPadrao(listaLog):
    opcao = {'Sala Exames/Sala Técnica': 1,
             'Sala Exames':2,
             'Sala Técnica':3,
             'Sala Adicional':4,
             'Tubo de Fluxo':5
             }
    try:
        limparResultados()
        graficoPreview(listaLog, opcao["Sala Exames/Sala Técnica"], caminhoCompleto=False)
        graficoPreview(listaLog, opcao["Tubo de Fluxo"], caminhoCompleto=False)
        print("Gráficos salvos na pasta resultados")
    except Exception as e:
        print(f"Erro: {e} ")
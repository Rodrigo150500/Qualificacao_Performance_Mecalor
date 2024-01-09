import os

def limparLogs():
    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resultado', 'LogsAtualizados'))
    arquivos = os.listdir(caminho)
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(caminho, arquivo)
        os.remove(caminho_arquivo)

import os
import sys
def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(os.path.abspath(__file__))
def limparResultados():

    print(f'Limpar Logs get {get_executable_path()}')
    #Limpando os logs antigos

    caminho = os.path.join(get_executable_path(),"Resultado/LogsAtualizados")
    caminhoQP = os.path.join(get_executable_path(), "Resultado/Qualificacao.xlsx")
    caminhoFoto = os.path.join(get_executable_path(), "Resultado/FotosGrafico")

    arquivos = os.listdir(caminho)

    print(f"Limpar Logs caminho {caminho}")
    print(f"Limpar Logs caminhoQP {caminhoQP}")
    print(f"Limpar Logs caminhoFoto {caminhoFoto}")
    #Deletando os resultados dos logs
    if len(arquivos) != 0:
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho, arquivo)
            os.remove(caminho_arquivo)

    #Deletando o resultado da planilha
    if os.path.exists(caminhoQP):
        os.remove(caminhoQP)

    #Deletando as imagens dos gráficos
    fotos = os.listdir(caminhoFoto)
    if len(fotos) > 0:
        for foto in fotos:
            caminhoNovo = os.path.join(caminhoFoto,foto)
            os.remove(caminhoNovo)


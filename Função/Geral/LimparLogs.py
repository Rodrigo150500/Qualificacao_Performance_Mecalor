import os
import sys
def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)
def limparResultados():

    #Limpando os logs antigos
    base_path = get_executable_path()
    caminho = os.path.join(base_path, 'Resultado/LogsAtualizados').replace("\\", "/")

    arquivos = os.listdir(caminho)
    if len(arquivos) != 0:
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho, arquivo)
            os.remove(caminho_arquivo)


    caminhoQP = os.path.join(get_executable_path(),'Qualificacao.xlsx').replace("\\", "/")
    print(f'Caminho {caminho}')
    print(f'Caminho QP{caminhoQP}')

    if os.path.exists(caminhoQP):
        os.remove(os.path.join(caminho,'Resultado/Qualificacao.xlsx')).replace("\\", "/")

    #Limpando as imagens dos logs novos

    caminhoFoto = (os.path.join(base_path, 'Resultado/FotosGrafico')).replace("\\", "/")
    
    fotos = os.listdir(caminhoFoto)
    if len(fotos) > 0:
        for foto in fotos:
            caminhoNovo = os.path.join(caminhoFoto,foto).replace("\\", "/")
            os.remove(caminhoNovo)

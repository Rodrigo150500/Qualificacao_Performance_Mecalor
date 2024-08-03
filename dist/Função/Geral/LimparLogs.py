import os

def limparResultados():

    #Limpando os logs antigos
    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Resultado', 'LogsAtualizados')) 


    arquivos = os.listdir(caminho)
    if len(arquivos) != 0:
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho, arquivo)
            os.remove(caminho_arquivo)

    caminhoQP = os.path.join(caminho,'../../Resultado/Qualificacao.xlsx') 

    if os.path.exists(caminhoQP):
        os.remove(os.path.join(caminho,'../../Resultado/Qualificacao.xlsx'))

    #Limpando as imagens dos logs novos
    caminhoFoto = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Resultado', 'FotosGrafico')) 
    
    fotos = os.listdir(caminhoFoto)
    if len(fotos) > 0:
        for foto in fotos:
            caminhoNovo = os.path.join(caminhoFoto,foto)
            os.remove(caminhoNovo)


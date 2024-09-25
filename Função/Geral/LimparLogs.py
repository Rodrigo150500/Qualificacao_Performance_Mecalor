import os
import sys
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado



def limparResultados():

    #Limpando os logs antigos

    caminho = os.path.join(acharCaminhoExecutado("Resultado/LogsAtualizados"))
    caminhoQP = os.path.join(acharCaminhoExecutado("Resultado/Qualificacao.xlsx") )
    caminhoFoto = os.path.join(acharCaminhoExecutado("Resultado/FotosGrafico"))

    arquivos = os.listdir(caminho)
    while True:
        try:
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
            break
        except:
            print("\nFECHE TODOS OS ARQUIVOS DA PASTA RESULTADOS!!!")
            print("NÃO CONSIGO REMOVER ARQUIVOS QUE ESTÃO EM USO")
            input("FECHE E ABRA NOVAMENTE...")


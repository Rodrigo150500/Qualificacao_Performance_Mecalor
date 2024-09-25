import os
import pandas as pd
import shutil
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado

def importarNovasAbas(dataFrameSalas, dataFrameTubo, nomeSalas, nomeTubo):


    #Diretorio original e diretorio para salvar
    caminhoExcel = os.path.normpath(os.path.join(acharCaminhoExecutado('Backup/Qualificacao.xlsx')))
    caminhoSalvar = os.path.normpath(os.path.join(acharCaminhoExecutado("Resultado")))



    shutil.copy(caminhoExcel,caminhoSalvar)

    caminhoCopia = os.path.join(caminhoSalvar, 'Qualificacao.xlsx')


    with pd.ExcelWriter (caminhoCopia, engine='openpyxl', mode='a') as writer:
        dataFrameSalas.to_excel(writer, sheet_name=nomeSalas, index=False)
        dataFrameTubo.to_excel(writer, sheet_name=nomeTubo, index=False)

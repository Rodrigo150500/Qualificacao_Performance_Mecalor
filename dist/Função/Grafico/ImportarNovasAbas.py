import os
import pandas as pd
import shutil

def importarNovasAbas(dataFrameSalas, dataFrameTubo, nomeSalas, nomeTubo):

    #Diretorio original e diretorio para salvar
    caminhoExcel = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../Backup/Qualificacao.xlsx')).replace("\\", "/")
    caminhoSalvar = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../Resultado')).replace("\\", "/")

    #Copiando e colando
    shutil.copy(caminhoExcel,caminhoSalvar)

    caminhoCopia = os.path.join(caminhoSalvar,'Qualificacao.xlsx').replace("\\", "/")


    with pd.ExcelWriter (caminhoCopia, engine='openpyxl', mode='a') as writer:
        dataFrameSalas.to_excel(writer, sheet_name=nomeSalas, index=False)
        dataFrameTubo.to_excel(writer, sheet_name=nomeTubo, index=False)


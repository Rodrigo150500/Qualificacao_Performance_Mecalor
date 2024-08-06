import os
import sys
import pandas as pd
import shutil

def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)


def importarNovasAbas(dataFrameSalas, dataFrameTubo, nomeSalas, nomeTubo):


    #Diretorio original e diretorio para salvar
    caminhoExcel = os.path.normpath(os.path.join(os.path.dirname(sys.executable), 'Backup/Qualificacao.xlsx'))
    caminhoSalvar = os.path.normpath(os.path.join(os.path.dirname(sys.executable), "Resultado"))



    shutil.copy(caminhoExcel,caminhoSalvar)

    caminhoCopia = os.path.join(caminhoSalvar, 'Qualificacao.xlsx')


    with pd.ExcelWriter (caminhoCopia, engine='openpyxl', mode='a') as writer:
        dataFrameSalas.to_excel(writer, sheet_name=nomeSalas, index=False)
        dataFrameTubo.to_excel(writer, sheet_name=nomeTubo, index=False)

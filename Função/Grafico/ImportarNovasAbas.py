import os
import pandas as pd
import shutil

import sys
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
    caminhoExcel = os.path.join(get_executable_path(),'Backup/Qualificacao.xlsx').replace("\\", "/")
    caminhoSalvar = os.path.join(get_executable_path(),'Resultado').replace("\\", "/")

    #Copiando e colando
    shutil.copy(caminhoExcel,caminhoSalvar)

    caminhoCopia = os.path.join(caminhoSalvar,'Qualificacao.xlsx').replace("\\", "/")

    print("Arquivo copiado\n")

    with pd.ExcelWriter (caminhoCopia, engine='openpyxl', mode='a') as writer:
        dataFrameSalas.to_excel(writer, sheet_name=nomeSalas, index=False)
        dataFrameTubo.to_excel(writer, sheet_name=nomeTubo, index=False)
    print("Dados escritos\n")

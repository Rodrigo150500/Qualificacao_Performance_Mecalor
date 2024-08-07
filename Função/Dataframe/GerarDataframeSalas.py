import os
import pandas as pd

import sys

from Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora

def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)

def gerarDataframeSalas(salaTecnica, salaExames, diretorio, nome, datas):

    logSalas = pd.read_csv(diretorio,sep=',')

    listaDataHora = gerarColunaDataHora(logSalas)

    leituraTempEquip = logSalas["TempEquip1 (C/10)"]/10
    leituraUmidEquip = logSalas["UmdEquip1 (UR/10)"]/10

    leituraTempExame = logSalas["TempExame1 (C/10)"]/10
    leituraUmidExame = logSalas["UmdExame1 (UR/10)"]/10

    dadosSalas = {
        'Data':listaDataHora[0],
        'Hora':listaDataHora[1],
        'Temp Equip Min (°C)':salaTecnica.minTemp,
        'Temp Equip Max (°C)':salaTecnica.maxTemp,
        'Temp Equip (°C)' : leituraTempEquip,
        'Umd Equip Min (%)' : salaTecnica.minUmid,
        'Umd Equip Max (%)' : salaTecnica.maxUmid,
        'Umd Equip (%)' : leituraUmidEquip,
        'Temp Exame Min (°C)' : salaExames.minTemp,
        'Temp Exame Max (°C)' : salaExames.maxTemp,
        'Temp Exame (°C)': leituraTempExame,
        'Umd Exame Min (%)':salaExames.minUmid,
        'Umd Exame Max (%)':salaExames.maxUmid,
        'Umd Exame (%)' : leituraUmidExame
    }

    colunasEquip = []
    colunasExame = []

    for coluna in dadosSalas:
        if "Equip" in coluna:
            colunasEquip.append(coluna)
        elif "Exame" in coluna:
            colunasExame.append(coluna)

    dataframeSalas = pd.DataFrame(data=dadosSalas)

    salvarDir = os.path.normpath(os.path.join(get_executable_path(),"Resultado/LogsAtualizados",nome))

    dataframeSalas.to_csv(salvarDir, index=False, sep=',', encoding="cp1252")

    dataframeSalasGrafico = dataframeSalas[dataframeSalas["Data"].isin(datas)].reset_index(drop=True)

    return dataframeSalas, colunasEquip, colunasExame, dataframeSalasGrafico


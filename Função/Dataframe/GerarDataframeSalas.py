import os
import pandas as pd
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado
from Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora


def gerarDataframeSalas(salaTecnica, salaExames, diretorio, nome, datas, arquivoTXT=False):

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

    if not arquivoTXT:

        dataframeSalas = pd.DataFrame(data=dadosSalas)

        salvarDir = os.path.normpath(os.path.join(acharCaminhoExecutado("Resultado/LogsAtualizados"),nome))

        dataframeSalas.to_csv(salvarDir, index=False, sep=',', encoding="cp1252")

        dataframeSalasGrafico = dataframeSalas[dataframeSalas["Data"].isin(datas)].reset_index(drop=True)

        return dataframeSalas, colunasEquip, colunasExame, dataframeSalasGrafico
    else:
        # Criando o DataFrame a partir do dicionário
        dataframeSalas = pd.DataFrame(data=dadosSalas)

        # Substituindo pontos por vírgulas nas colunas específicas
        colunas_substituir = ["Temp Equip (°C)", "Umd Equip (%)", "Temp Exame (°C)", "Umd Exame (%)"]
        dataframeSalas[colunas_substituir] = dataframeSalas[colunas_substituir].astype(str).apply(lambda x: x.str.replace('.', ','))

        # Definindo o diretório para salvar o arquivo
        salvarDir = os.path.normpath(os.path.join(acharCaminhoExecutado("Resultado/LogsAtualizados"), nome))

        # Salvando o DataFrame como arquivo .csv com ";" como separador
        dataframeSalas.to_csv(salvarDir, index=False, sep=';', encoding="cp1252")

        # Filtrando os dados para gerar o gráfico
        dataframeSalasGrafico = dataframeSalas[dataframeSalas["Data"].isin(datas)].reset_index(drop=True)

        return



import os
import pandas as pd


def verificarLog(salaExames, salaTecnica, listaLog):
    #Fazer uma condição para ler apenas o log de exames conforme foi selecionado

    logDiretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logs'))
    logs = os.listdir(logDiretorio)


    for opcao in listaLog:
        for log in logs:
            if(opcao[1] == log and opcao[0] == 1):

                diretorio = os.path.join(logDiretorio,log)
                gerarLog(salaExames, salaTecnica, diretorio)


def gerarLog(salaExames, salaTecnica, log):
    dados = pd.read_csv(log, sep=',')

    dataHoras = dados.Data.unique()
    listaData = []
    listaHora = []
    for dataHora in dataHoras:
        dia = str(dataHora)[4:6]
        mes = str(dataHora)[2:4]
        ano = str(dataHora)[0:2]

        hora = str(dataHora)[6:8]
        min = str(dataHora)[8:10]
        seg = str(dataHora)[10:12]

        data = f"{dia}/{mes}/{ano}"
        horario = f"{hora}:{min}:{seg}"

        listaData.append(data)
        listaHora.append(horario)

    #Criando as colunas de Data e Hora
    dados["Data2"] = listaData
    dados["Hora"] = listaHora

    #Criando as colunas da Sala Técnica
    dados = dados.rename(columns={"TempEquip1 (C/10)": "Temp Equip (°C)"})
    dados = dados.rename(columns={"UmdEquip1 (UR/10)": "Umid Equip (%)"})
    dados["Temp Equip Min (°C)"] = salaTecnica.minTemp
    dados["Temp Equip Max (°C)"] = salaTecnica.maxTemp
    dados["Umid Equip Min (%)"] = salaTecnica.minUmid
    dados["Umid Equip Max (%)"] = salaTecnica.maxUmid


    #Criando as colunas da Sala de Exame
    dados = dados.rename(columns={"TempExame1 (C/10)":"Temp Exame (°C)" })
    dados = dados.rename(columns={"UmdExame1 (UR/10)":"Umid Exame (%)" })
    dados["Temp Exame Min (°C)"] = salaExames.minTemp
    dados["Temp Exame Max (°C)"] = salaExames.maxTemp
    dados["Umid Exame Min (%)"] = salaExames.minUmid
    dados["Umid Exame Max (%)"] = salaExames.maxUmid

    #Excluindo as colunas desnecessárias
    dados.drop(['DewEquip1 (C/10)',
       'TempEquip2 (C/10)', 'UmdEquip2 (UR/10)', 'DewEquip2 (C/10)',
       'DewExame1 (C/10)',
       'TempExame2 (C/10)', 'UmdExame2 (UR/10)', 'Unnamed: 12',
      ], axis=1, inplace=True)


    #Reorganizando as colunas
    dados = dados[['Data','Data2','Hora',
                                  
                   'Temp Equip Min (°C)',
                   'Temp Equip Max (°C)',
                   'Temp Equip (°C)',

                   'Umid Equip Min (%)',
                   'Umid Equip Max (%)',
                   'Umid Equip (%)',

                   'Temp Exame Min (°C)',
                   'Temp Exame Max (°C)',
                   'Temp Exame (°C)',

                   'Umid Exame Min (%)',
                   'Umid Exame Max (%)',
                   'Umid Exame (%)',
]]

    #Dividindo as colunas da leitura por 10
    dados["Temp Equip (°C)"] = dados["Temp Equip (°C)"]/10
    dados["Umid Equip (%)"] = dados["Umid Equip (%)"]/10

    dados["Temp Exame (°C)"] = dados["Temp Exame (°C)"]/10
    dados["Umid Exame (%)"] = dados["Umid Exame (%)"]/10

    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resultado',"LogsAtualizados"))
    nomeLog = os.path.join(caminho,"logSalas.txt")

    dados.to_csv(nomeLog, index=False, sep=';', encoding="cp1252")

def gerarGrafico():
    pass

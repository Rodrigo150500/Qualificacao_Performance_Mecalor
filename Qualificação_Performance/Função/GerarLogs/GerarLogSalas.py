import os
import pandas as pd
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Logs.GerarColunaDataHora import gerarColunaDataHora
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Logs.GerarColunaSalaTecnica import gerarColunaSalaTecnica
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Logs.GerarColunaSalaExame import gerarColunaSalaExame

def gerarLogSalas(salaExames, salaTecnica, log):
    dados = pd.read_csv(log, sep=',')

    #Gerando as colunas de data e hora
    dados = gerarColunaDataHora(dados)

    #Criando as colunas da Sala Técnica
    dados = gerarColunaSalaTecnica(dados, salaTecnica)

    #Criando as colunas da Sala de Exame
    dados = gerarColunaSalaExame(dados, salaExames)

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

    #Definindo o caminho para salvar o novo Log atualizado
    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Resultado', "LogsAtualizados"))
    nomeLog = os.path.join(caminho,"logSalas.txt")

    dados.to_csv(nomeLog, index=False, sep=';', encoding="cp1252")




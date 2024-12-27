import os
import pandas as pd
from Função.GerarColunas.GerarColunaDataHora import gerarColunaDataHora
from Função.GerarColunas.GerarColunaSalaTecnica import gerarColunaSalaTecnica
from Função.GerarColunas.GerarColunaSalaExame import gerarColunaSalaExame
def gerarLogSalas(salaExames, salaTecnica, diretorio, nome):
    dados = pd.read_csv(diretorio, sep=',')

    # Gerando as colunas de data e hora
    dados = gerarColunaDataHora(dados)

    # Criando as colunas da Sala Técnica
    dados = gerarColunaSalaTecnica(dados, salaTecnica)

    # Criando as colunas da Sala de Exame
    dados = gerarColunaSalaExame(dados, salaExames)

    # Excluindo as colunas desnecessárias
    dados.drop(['DewEquip1 (C/10)',
                'TempEquip2 (C/10)', 'UmdEquip2 (UR/10)', 'DewEquip2 (C/10)',
                'DewExame1 (C/10)',
                'TempExame2 (C/10)', 'UmdExame2 (UR/10)', 'Unnamed: 12',
                ], axis=1, inplace=True)

    # Reorganizando as colunas
    dados = dados[['Data', 'Data2', 'Hora',
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

    # Dividindo as colunas da leitura por 10
    colunas_dividir_por_10 = ["Temp Equip (°C)", "Umid Equip (%)", "Temp Exame (°C)", "Umid Exame (%)"]
    dados[colunas_dividir_por_10] /= 10

    # Substituindo pontos por vírgulas nas colunas específicas
    colunas_substituir = ["Temp Equip (°C)", "Umid Equip (%)", "Temp Exame (°C)", "Umid Exame (%)"]
    dados[colunas_substituir] = dados[colunas_substituir].astype(str).apply(lambda x: x.str.replace('.', ','))

    # Definindo o caminho para salvar o novo Log atualizado
    caminhoPath =  os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'Resultado', "LogsAtualizados"))
    caminho = caminhoPath.replace("\\", "/")
    nomeLog = os.path.join(caminho, nome)

    dados.to_csv(nomeLog, index=False, sep=';', encoding="cp1252")


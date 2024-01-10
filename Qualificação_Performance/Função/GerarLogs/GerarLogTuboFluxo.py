import os
import pandas as pd
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Logs.GerarColunaDataHora import gerarColunaDataHora
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Logs.GerarColunaTuboFluxo import gerarColunaTuboFluxo

def gerarLogTuboFluxo(tuboFluxo, log):
    dados = pd.read_csv(log, sep=',')

    #Gerando a coluna de data e hora
    dados = gerarColunaDataHora(dados)

    #Gerando a coluna do tubo de Fluxo
    dados = gerarColunaTuboFluxo(dados=dados,tuboFluxo=tuboFluxo)

    #Excluindo as colunas desnecessárias

    #Reorganizando as colunas

    #Dividindo as colunas por 10

    #Definindo o caminho para salvar o novo log atualizado
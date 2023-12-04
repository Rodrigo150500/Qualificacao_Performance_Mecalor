import pandas as pd

dir = 'aluguel.csv'

dados = pd.read_csv(dir, sep=';')

#Filtrando a tabela onde apenas tenha 1 quarto
selecao1 = dados['Quartos'] == 1
print(dados[selecao1])

#Filtrando a tabela onde o valor é menos que 3000
selecao2 = dados['Valor'] < 3000
print(dados[selecao2])

#Filtrando com mais de uma condição
selecao = (dados['Quartos'] == 1) & (dados['Valor'] < 3000)
print(dados[selecao])
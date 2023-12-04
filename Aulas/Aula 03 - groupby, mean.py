import pandas as pd

dir = "aluguel.csv"

dados = pd.read_csv(dir, sep=';')


#Pegando os valores medio da coluna valor
print(dados['Valor'].mean())

#Pegando o valor medio de cada aluguel porem com apenas os valores numericos
print(dados.groupby('Tipo').mean(numeric_only=True))

#Pegando apenas a coluna valor de cada tipo
print(dados.groupby('Tipo')['Valor'].mean())

#Agrupando os valores da coluna tipo e fazendo a media de cada tipo de aluguel e deixando em ordem crescente
print(dados.groupby('Tipo')['Valor'].mean().sort_values())

df_preco_tipo = dados.groupby('Tipo')['Valor'].mean().sort_values()

df_preco_tipo.plot(kind = "barh", figsize=(14,10), color="purple")


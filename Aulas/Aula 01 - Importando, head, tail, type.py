import pandas as pd

url = "aluguel.csv"

dados = pd.read_csv(url, sep=';')

#Imprime as 5 primeiras linhas e pode ser parametrizado para add mais linhas
print(dados.head())

#Imprime as últimas 5 linhas e pode ser parametrizado para add mais linhas
print(dados.tail())

#Imprime o tipo de dado
print(type(dados))
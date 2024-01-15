import pandas as pd

url = "aluguel.csv"

dados = pd.read_csv(url, sep=';')

#Imprime o numero de linhas e colunas
print(dados.shape)

#Imprime as colunas
print(dados.columns)

#Imprime os tipos de dados que são cada coluna
print(dados.info())

#Imprimindo apenas uma coluna
print(dados["Tipo"])

#Imprimindo duas colunas
print(dados[["Tipo", "Valor"]])


import pandas as pd

dir = "aluguel.csv"

dados = pd.read_csv(dir, sep=';')
print(dados)


#Mostra True ou False se o dado é nulo ou não
print(dados.isnull())

#Mostra a quantidade de dados nulos
print(dados.isnull().sum())

#Substituindo os valores null por 0
dados = dados.fillna(0)
print(dados.isnull().sum())

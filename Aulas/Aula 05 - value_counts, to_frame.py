import pandas as pd

dir = "aluguel.csv"

dados = pd.read_csv(dir,sep=';')

#Mostra a quantidade de cada Tipo
qtda = dados.Tipo.value_counts()
print(qtda)

#Mostrando o percentual de cada imovel
percentual = dados.Tipo.value_counts(normalize=True)
print(percentual)

#Transformando de Series para Frame em ordem decrescente
dataFrame = percentual.to_frame().sort_values('Tipo')
print(dataFrame)

#Selecionando apenas um tipo de imovel nesse caso apartamento
ap = dados.query('Tipo == "Apartamento"')
print(ap.head())
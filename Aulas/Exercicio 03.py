import pandas as pd

dir = "aluguel.csv"

dados = pd.read_csv(dir,sep=';')


#Imprimindo a coluna de Tipos e mostrando quantas vezes tem cada imovel
tipo = dados['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')
print(tipo)

tipo.rename(columns={'Tipo':'Percentuais'}, inplace=True)
print(tipo)
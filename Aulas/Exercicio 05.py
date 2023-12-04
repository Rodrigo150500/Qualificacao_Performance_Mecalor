import pandas as pd

dados = pd.DataFrame([['Feira', 'Cebola', 2.5],
                        ['Mercado', 'Cebola', 1.99],
                        ['Supermercado', 'Cebola', 1.69],
                        ['Feira', 'Tomate', 4],
                        ['Mercado', 'Tomate', 3.29],
                        ['Supermercado', 'Tomate', 2.99],
                        ['Feira', 'Batata', 4.2],
                        ['Mercado', 'Batata', 3.99],
                        ['Supermercado', 'Batata', 3.69]],
                        columns = ['Local', 'Produto', 'Preço'])

#Removendo as linhas que possuem mercado
indexRemove = dados.query("Local == 'Supermercado'").index
print(indexRemove)
dados.drop(indexRemove, axis=0, inplace=True)

print(dados)
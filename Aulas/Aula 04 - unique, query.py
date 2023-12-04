import pandas as pd

dir = "aluguel.csv"

dados = pd.read_csv(dir, sep=';')

#Mostra os dados da coluna Tipo
print(dados.Tipo.unique())

lista_imoveis = ["Conjunto Comercial/Sala",
                 "Flat",
                 "Loja/Salão",
                 "Galpão/Depósito/Armazém",
                 "Terreno Padrão",
                 "Box/Garagem",
                 "Loft",
                 "Loja Shopping/ Ct Comercial",
                 "Studio",
                 "Indústria"]

#Mostra os dados que não estão na lista
print(dados.query("@lista_imoveis not in Tipo"))


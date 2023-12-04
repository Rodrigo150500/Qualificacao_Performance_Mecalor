import pandas as pd

df = pd.DataFrame({
   'Animal': ['Cachorro', 'Gato', 'Elefante', 'Cachorro', 'Gato', 'Elefante'],
   'Cor': ['Preto', 'Branco', 'Cinza', 'Marrom', 'Preto', 'Marrom'],
   'Quantidade': [2, 3, 1, 4, 2, 2]
})

animais = df.groupby("Animal").sum(numeric_only=True)
print(animais)


quantidade = df.groupby(["Animal", "Cor"])[['Quantidade']].sum()
print(quantidade)
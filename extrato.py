import pandas as pd

df = pd.read_csv('./files/data.csv')

valido = df.query('Categoria=="Execução de ordem"')

# btc = valido.groupby('Moeda').groups['BTC']
moeda = valido.groupby('Moeda').agg(lambda x: list(set(x))).reset_index()
print(moeda.filter)
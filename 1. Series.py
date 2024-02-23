import pandas as pd

#1-Dados dos times e qtd de titulos
data = {
    'Palmeiras' : 12,
    'São Paulo' : 6,
    'Corinthians': 7,
    'Santos': 8
}
print('\n')

#2-Criando serie a partir de um dicionario
series_times = pd.Series(data)
print(series_times)

print('\n')

#3-Selecionando por Time
print(series_times['Palmeiras'])
print(series_times.iloc[3]) 

print('\n')

#4-Selecionando por Fatiamento
print(series_times['Palmeiras':'Corinthians']) #inclusivo (contem o primeiro e o ultimo item)

print('\n')

#5-Selecionando por condição
print(series_times[series_times > 7])
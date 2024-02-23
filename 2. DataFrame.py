import pandas as pd

#1-Dados dos times e qtd de titulos
tt = {
    'Palmeiras' : 12,
    'São Paulo' : 6,
    'Corinthians': 7,
    'Santos': 8
}
print('\n')

#2-Ano do Titulo
dt = {
    'Palmeiras' : [1960,1993,1994,2016,2018,2022,2023],
    'São Paulo' : [2006,2007,2008,1996],
    'Corinthians': [2005,2017,2015,1998],
    'Santos': [1968,1969,1990,2000]
}
print('\n')

#3-Criando a Series
serie_titulos = pd.Series(tt)
serie_anos = pd.Series(dt)

#4-Criando DataFrame combinando as Series
data = {'Titulos': serie_titulos, 'Anos': serie_anos}
dataframe_times = pd.DataFrame(data)

#5-Exibindo DataFrame
print(dataframe_times)
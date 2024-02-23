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
    'Palmeiras' : [1969,1993,1994,2016,2018,2022,2023],
    'São Paulo' : [1969,2006,2007,2008,1996],
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

print('\n')

#1-Média de Titulos
media_titulos = dataframe_times['Titulos'].mean()
print(f'Média de Titulos: {media_titulos}')

print('\n')

#2-Mais de Titulos
mais_titulos = dataframe_times['Titulos'].idxmax()
qtd = dataframe_times['Titulos'].max()
print(f'Time com mais titulos é {mais_titulos} com {qtd} titulos')

print('\n')

#3-Ano com mais titulos
all = dataframe_times['Anos'].explode()
ano_mais_titulos = all.mode()[0]
qtd_ano = dataframe_times['Anos'].explode().value_counts().idxmax()
print(f'Ano com mais títulos: {ano_mais_titulos}, quantidade = {qtd_ano}')

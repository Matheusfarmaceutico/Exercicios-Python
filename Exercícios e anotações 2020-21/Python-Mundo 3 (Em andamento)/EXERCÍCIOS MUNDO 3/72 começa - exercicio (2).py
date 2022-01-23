#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

VINTE=('FLAMENGO','SANTOS','PALMEIRAS','GRÊMIO','ATHLETICO-PR','SÃO PAULO','INTERNACIONAL','CORINTHIANS','FORTALEZA','GOIÁS','BAHIA','VASCO DA GAMA','ATLÉTICO-MG','FLUMINENSE',
'BOTAFOGO','CEARÁ SC','CRUZEIRO','CSA','CHAPECOENSE', 'AVAÍ')
print('-='*145)
print(f'Os vinte primeiros times do brasileirão: {VINTE}')
print('-='*145)
print(f'Os cinco primeiros colocados: {VINTE[0:5]}')
print('-='*145)
print(f'Os últimos quatro colocados: {VINTE[16:21]}')
print('-='*145)
print(F'Os times por ordem alfabética: {sorted(VINTE)}')
print('-='*145)
print('A chapecoense ocupa a posição {}'.format(VINTE.index('CHAPECOENSE')+1))

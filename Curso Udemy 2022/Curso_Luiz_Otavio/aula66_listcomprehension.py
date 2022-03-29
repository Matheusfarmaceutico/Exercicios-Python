''''l1 = [1,2,3,4,5]
l2 = [variaveis for variaveis in l1]
print(l2)'''

"""l1 = [1,2,3,4,5]
l2 = [var * 2 for var in l1] #multiplicando cada valor da minha l1 por 2, atraves de listcomprehension.
print(l2)"""
"""l1 = [1,2,3,4,5]
coordenadas = [(v1,v2)for v1 in l1 for v2 in range(3) ]
print(coordenadas)"""

"""nomes = ["Mauro","Matheus","Renata","Alberto"]
l2 = [arroba.replace("a","@") for arroba in nomes ]
print(l2)"""

"""#invertendo chave e valor
"1. Original"

tupla = (
    ("chave","valor"),
    ('chave2',"valor2"))
inverter = [(chave,valor) for chave, valor in tupla]
print(inverter)
"2.Modificado-inversao"
tupla = (('Aluno','Matheus'),)
inverter = [(valor,chave) for chave, valor in tupla]
print(inverter)
"3. convertendo para dicionarios"

inverter = dict(inverter)
print(inverter)"""

#com condicoes
#1 - Com apenas uma condicao"

"""contagem = list(range(100))
divisivel_por_2 = [divisivel for divisivel in contagem if divisivel % 2 == 0]
print(divisivel_por_2)"""

#2 - Com mais de uma condicao"
"""contagem = list(range(100))
divisil_dois_oito = [divisiveis for divisiveis in contagem if divisiveis % 3 == 0 if divisiveis % 8 == 0]
print(divisil_dois_oito)"""

#3 - Utilizando else


"""contagem = list(range(100))
com_else = [divisivel if divisivel % 3 == 0 else 'nao é' for divisivel in contagem]
print(com_else)"""


# RESUMO DA ORDEM UTILIZADA COM UMA E A PARTIR DE DUAS CONDICOES, E COM ELSE

'''lista = list(range(100))
# Com uma condicao
one = [n for n in lista if n % 2 == 0]
print(one)
print()'''
#com duas condições

'''lista = list(range(100))
two = [n for n in lista if n % 2 == 0 if n % 3 == 0]
print(two)'''

#com else (if primeiro)

'''lista = list(range(100))
senao = [n if n != 13 else "e 13 memo" for n in lista]
print(senao)'''
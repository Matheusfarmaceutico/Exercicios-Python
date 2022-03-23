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

#invertendo chave e valor
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
print(inverter)

tupla = [{'Aluno':'Matheus',"Aluno02":"Lucas"}]
inverter = [(valor,chave) for chave, valor in tupla]
print(inverter)
"""
s1 = {1,2,3,4} set em python, conta somente com valor, não chave."""




"""s1 = set()
s1.add(1)
s1.add(2)
s1.add((4,5,6,'Matheus')) # adicionei uma tupla ao meu set
s1.discard(2) #remove um elemento
s1.update('python') #itera sobre a string informada, não respeitando ordem. P Y T H O N ou N O H T Y P...
print(s1)"""

"""#sets não consideram elementos duplicados
s1 = {1,2,2}
print(s1) # saída é 1,2
print(len(s1))
s1.update([1,2,3,4])
print(s1)
print(type(s1))"""

'''s1 = {1,2,3}
s2 = {4,5,6}
print(s1|s2) #juntando'''

'''s1 = {1,2,3,4}
s2 = {1,2,3}
s3 = s1 & s2 # intersection = todos os elementos comuns nos dois sets. Uso do & comercial
print(s3)'''

'''s1 = {1,2,3,4,5}
s2 = {1,2,3,4,6}
s3 = s1 - s2 #difference: O sinal - mostra qual o elemento distinto que está à esquerda. Se inverter, o resultado muda, mas sempre à esquerda
print(s3)
s3 = s2 - s1
print(s3)'''

'''s1 = {1,2,3,4,5}
s2 = {1,2,3,4,6}
s3 = s2 ^ s1 # symmetric_difference = ^ vai mostrar elementos elementos incomuns nos dois sets
print(s3)'''


#A diferença entre difference(-) e symmetric_difference é que no caso do primeiro, são exibidos apenas os resultados assimétricos do que está à esquerda do sinal (-), ao passo que symmetric_difference são exibidos valores simétricos.

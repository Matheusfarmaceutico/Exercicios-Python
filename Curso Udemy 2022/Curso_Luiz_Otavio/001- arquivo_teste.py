s1 = {1,2,3,4,5}
s2 = {1,2,3,4,6}
s3 = s1 - s2 #difference: O sinal - mostra qual o elemento distinto que está à esquerda. Se inverter, o resultado muda, mas sempre à esquerda
print(s3)
s3 = s2 - s1
print(s3)

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,6}
s3 = s2 ^ s1 # symmetric_difference = ^ vai mostrar elementos elementos incomuns nos dois sets
print(s3)
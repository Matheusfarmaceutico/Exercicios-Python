def separador():
    return "-="*30
"""count - itertools"""
# Apresentação do count
from itertools import count
# aceita número de ponto flutuante como step, mas n aceita um limite.
contador = count(start=5, step=0.05)
for v in contador:

    print(round(v, 2))  # arredonda em duas casas decimais
    if v > 10:
        break
print(separador())
contador = count()
nomes = ['Matheus','Júlia','Rafaela']
nomes = zip(contador,nomes)
for v in nomes:
    print(v[0], v[1])
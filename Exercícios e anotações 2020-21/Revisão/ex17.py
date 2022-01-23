from math import hypot
o=float(input('Digite o cateto oposto: '))
adjacente=float(input('Digite o cateto adjacente: '))
print(f"O comprimento da hipotenusa é de {hypot(o, adjacente):.2f} cm")
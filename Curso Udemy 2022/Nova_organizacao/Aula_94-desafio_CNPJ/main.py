import cnpj
"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

def contador(sem_digitos):
    lista = []
    for v in sem_digitos:
        v = int(v)
        lista.append(v * len(sem_digitos))
    return lista
        


contador("04252011000110")


 def contagem():
        valores = []
        if len(arg) == 12:
            valores.append(5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
        elif len(arg) == 13:
            valores.append(6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
        
        
    return contagem
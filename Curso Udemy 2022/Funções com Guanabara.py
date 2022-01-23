"""def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


titulo('    MATHEUS ALVES   ')"""

"""def calculadora(a, b):
    if option == 'S':
        return print(a + b)
    elif option == 'M':
        return print(a * b)
    elif option == 'D':
        return print(a / b)


n1 = int(input('N1:'))
n2 = int(input('N2: '))
option = str(input('Gostaria de s,m ou d?: ')).strip().upper()
calculadora(n1, n2)"""

# desemacotamento de parâmetros python
"""def contador(*num):
    print(num)


contador(2, 3, 4, 6)
contador(2, 4, 6,4,4,'5')"""

#utilização de listas
def dobrar(lista):
    c = 0
    while c < len(lista):
        lista[c] *= 2
        c += 1
    print(lista)


valores = [2, 3, 4, 5, 10, 8, 5]
dobrar(valores)


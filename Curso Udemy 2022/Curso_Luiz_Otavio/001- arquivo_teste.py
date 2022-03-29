lista = list(range(100))
# Com uma condicao
one = [n for n in lista if n % 2 == 0]
print(one)
print()
#com duas condições

two = [n for n in lista if n % 2 == 0 if n % 3 == 0]
print(two)

#com else (if primeiro)


senao = [n if n != 13 else "e 13 memo" for n in lista]
print(senao)
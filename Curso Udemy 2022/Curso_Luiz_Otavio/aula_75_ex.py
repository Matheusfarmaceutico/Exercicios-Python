def separador():
    print("-="*30)
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]"""
separador()
#Minha solução (mais pythonica)
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
temp = zip(lista_a,lista_b)
for v in temp:
    print(sum(v))
separador()

# Maneira mais lógica, comum a todas as linguagens
lista_soma = []
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)
separador()

#Uma outra maneira mais lógica, assim assim utilizando o enumerate, que está presente apenas no Python

lista_soma = []
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

separador()


#solucao do Luiz Otávio, julguei ser mais certa e correta, utilizando um modo ainda mais pythonico que o que eu desenvovi.

lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
lista_soma = [x + y for x,y in (zip(lista_a, lista_b))]
print(lista_soma)



"""lista = [1,2,3,4,5]
print(*lista, sep= '-')
#desempacotando e separando"""

"""def convert(*lista):
    lista = list(lista) # conversão de uma tupla (valor devolvido normalmente, para ser mutável)
    lista[0] = 20
    print(lista)
convert(1,2,3,4,5)"""

"""def desempacotar(*args):
    args = list(args)
    print(args)
lista = [1,2,3,4,5]
desempacotar(*lista) # (lista) ao invés de (*lista) faz com que meu resultado seja: ([1,2,3,4,5]). Mas (*lista) desempacota minha lista, e posso continuar adicionando termos."""

#kargs (devolve dicionário)

"""def desempacotar(*args, **kargs):
    args = list(args)
    print(args)
    print(kargs['sobrenome'])
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
desempacotar(*lista1, *lista2, nome ='Matheus',sobrenome = 'Alves' )"""

#outra maneira de acessar dicionários de def

def desempacotar(*args, **kargs):
    args = list(args)
    print(args)


    idade = kargs.get('Idade') #O get() é um método usado para pegar o valor de uma dada chave em um dicionário se a chave estiver no dicionário, caso ela não exista, o método retorna None ou o valor padrão passado por parâmetro.
    if idade is not None:
        print(idade)
    else:
        print('Idade não cadastrada!')

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
desempacotar(*lista1, *lista2, nome = 'Matheus', sobrenome = 'Alves', Idade = 23)

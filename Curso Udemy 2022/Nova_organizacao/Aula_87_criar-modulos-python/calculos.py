import math

PI= math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


lista = [1,2,3,4,5]




def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r
if __name__ == "__main__":
    print(multiplica(lista))
    print(PI)
    print(dobra_lista(lista))


print(__name__)
## Observe que quando eu executo um arquivo com __name__ printado, ele é representado por __main__. Contudo,
## quando o módulo este arquivo é carregado como um módulo em um outro arquivo, esse print é chamado e aparece o nome do arquivo de origem, nesse caso "calculos". Dessa forma, criei uma condic onde se o arquivo printado for __main__ ele irá aparecer na tela, caso se trate de um outro arquivo que o esteja chamando como um módulo, nao haverá print.
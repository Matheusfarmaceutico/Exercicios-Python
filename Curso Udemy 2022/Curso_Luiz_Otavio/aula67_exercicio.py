




string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

def separador(args):
    lista = [args[i: i + 10] for i in range(0,len(string), 10)]
    return ".".join(lista)


print(separador(string))
print("teste")





string = '01234567890123456789012345678901234567890123456789'

def separador(arg):
    arg = [arg[i: i + 10] for i in range(0, len(arg),10)]
    return ".".join(arg)


print(separador(string))
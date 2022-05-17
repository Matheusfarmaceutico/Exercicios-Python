from separador import separador

# Try-except como condicionais.
def converter_numero(numero):
    try:
        numero = int(numero)
        return numero
    except ValueError:
        try:
            numero = float(numero)
            return numero
        except:
            pass #Retorna None
while True:
    n = converter_numero(input("Digite um número: "))
    if n is not None: 
        print(n * 5)
        break
    else:
        print("Isso nao é um número! Tente novamente")
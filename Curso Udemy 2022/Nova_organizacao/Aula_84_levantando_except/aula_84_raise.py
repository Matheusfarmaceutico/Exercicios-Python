# Exceções padroes do Python
# https://docs.python.org/3/library/exceptions.html
from separador import separador
# 1 - Tratando exceções de divisão por 0

print(separador())
print("1 - Tratando exceções de divisão por 0")
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        return error


print(divide(2,0))

print(separador())

# 2 - Relançando exceções com raise

print("2 - Relançando exceções com raise")

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(f"Log: {error}")
        raise
        

try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print("Sem raise nao vai aparecer")

print(separador())

# 3 - Customizando o lançamento de exceções com raise

print("3 - Customizando o lançamento de exceções com raise")

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Divisão por 0 impossível")
    return n1 / n2

try:
    print(divide(2,5))
except ValueError as error:
    print("Você tentou dividir um valor por 0, tente novamente!")
finally:
    print("sempre executada")
print("continua")
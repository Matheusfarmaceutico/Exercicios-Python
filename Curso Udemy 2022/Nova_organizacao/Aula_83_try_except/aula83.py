
from ast import Continue
from decimal import DivisionByZero
from tkinter import EXCEPTION
from typing import final
from pyrsistent import b
from separador import separador

# Note que é uma boa prática especificar o erro, e nao apenas utilizar o except sem especificar nada.
# Veja que quando vc cria uma excecao para um erro específico, os outros n serão filtrados. Caso eu especifique para TypeError, por exemplo, e eu cometa um erro de tipo, meu código continuará a ser executado.
# O problema é que isso n vai acontecer se o erro for outro, como StopIteration, NameError.
# 


print("Try e except - Exemplo 01")
try:
    print('a' + 2)
except TypeError as error:
    print(f"Tipo de erro: {error}")

print("Código continua")
print(separador())
#Não daria certo (n daria para continuar o código, porque esperava-se um erro de NameError e ocorreu um erro de TypeError):
"""try:
    print('a' + 2)
except NameError as error:
    print(error)

print("continua")"""

#Contudo, eu poderia levantar outros except possíveis
print("Try e except - Exemplo 02")
try:
    print(a)

    
except (IndexError, NameError) as errou1:
    print(f"Tipo de erro: {errou1}")

print("Continua")
print(separador())

print("Try e Except - Exemplo 03")
# Posso utilizar Finally. Ele é executado com o código dentro de try estando correto ou nao


try:
    a = 2/0

except Exception as error:
    print(f"Erro inesperado: {error}")

else:
    print("Só serei executado se n houver erro ")

finally:
    print("Sempre serei executado")
print("continua")
print(separador())
print("Try e Except - Exemplo 04")

# Posso utilizar Finally para que se um valor que n foi criado dentro do try por conta de um erro, seja criado dentro dele e uma outra excecao nao seja levantada. 


try:
    a = 2/0 # Nesse caso a variavel "a" nao será criada, por conta de um erro. Finally a criará embaixo para suprimir o problema.

except Exception as error:
    print(f"Erro inesperado: {error}")

else:
    print("Só serei executado se n houver erro ")

finally:
   a = None
print(a)
print("continua")




"""Em algum momento, você pode fazer algo no try que precisa ser finalizada, por exemplo, abrir um arquivo, abrir um conexão de rede, etc etc... Essas coisas abertas precisam ser fechadas, porém, se houver erros antes de atingir o código de fechamento, o que você abriu nunca será fechado. Então, é uma boa prática de programação, assumir que o que você está fazendo pode gerar erros e usar o bloco finally para finalizar/fechar o que tinha aberto antes."""



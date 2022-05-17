# 01 - Eu consigo sobrescrever um módulo através de uma funcao 
from random import randint
print(randint(0,10))

def randint(*args):
    return "hahah"

print(randint())
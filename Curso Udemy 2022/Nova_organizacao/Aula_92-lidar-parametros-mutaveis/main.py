from typing import Tuple


def clientes(iteravel,lista=Tuple):
    if lista is Tuple:
        lista = []
    lista.extend(iteravel)
    return lista


cliente1 = clientes(["Alberto","DINATA"])
cliente2 = clientes(["Henrique","Fenix"])
print(cliente1)

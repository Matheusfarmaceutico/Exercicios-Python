# Exercício: criar uma funcao decoradora que calcula o tempo de execucao de uma outra funcao

from time import sleep
from time import time

def func_contagem(funcao):
    def clock(*args,**kargs):
        start = time()
        termino = funcao(*args,**kargs)
        end = time()
        tempo_gasto = (end - start) * 1000
        print(f"A função {funcao.__name__} demorou {tempo_gasto:.2f} ms para ser executada")
        return termino
    return clock

@func_contagem
def func_execucao():
    for i in range(5):
        print(i)
        sleep(1)

func_execucao()
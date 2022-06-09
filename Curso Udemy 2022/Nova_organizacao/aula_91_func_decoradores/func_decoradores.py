"""

1 - Chamando uma variavel como uma funcao
def fala_oi():
    print("oi")
    


variavel = fala_oi
print(variavel()) #chamando uma variavel que é uma func"""

"""#2 - Chamando uma funcao que está dentro de outra funcao
def master():
    def slave():
        return "oi"
    return slave #tenho que chamar dentro da funcao mae

variavel = master()
print(variavel())"""


# exemplo 03 - funcao decoradora


def master(funcao):
    
    def slave():
        print("Agora estou decorada")
        funcao()
    return slave


@master # ou posso usar: fala_oi = master(fala_oi) ou 
def fala_oi():

    print("oi")

fala_oi() # Esta é por si só uma func DECORADORA"""



"""# Exemplo 04 - Decoradores com funcoes com argumentos
def master(funcao):
    
    def slave(*args,**kargs): #inicialmente slave nao leva argumento, por isso quando decoro outra func com master, da erro.
        print("Agora estou decorada")
        funcao(*args,**kargs)
    return slave


@master
def outra_func(msg):
    print(msg)


outra_func("Amigo estou aqui")"""

# Exemplo 05 - Testando a velocidade com o que uma func é executada

from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo_gasto = (end_time - start_time) * 1000
        print(f"A função {funcao.__name__} levou {tempo_gasto:.2f} ms para ser executada")
        return resultado
    return interna


@velocidade
def demora():
    for i in range(5):
        sleep(1)


demora()

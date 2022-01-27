variavel = 'valor'
#Exemplo 01
""" def escopo_local():
    variavel = 'outro valor'
    print(variavel)


escopo_local()"""

#Exemplo 02 - alterando variáveis globais a partir de definições locais. (Prática não recomendada)

"""def alterando_var_global():
    global variavel
    variavel = 'Valor alterado'
print(variavel) #veja como antes da função chamada a variavel = valor quando printada responde como 'valor'.
alterando_var_global() #note que a variavel global só é alterada quando a função é chamada, não quando ela é criada.
print(variavel)"""

# Exemplo 03 - Ao invés disso, é mais correto eu alterar a var global apenas dentro do escopo local,
#para não gerar bugs em meu programa.

"""def escopo_local_legal(args = None):
    args= args.replace('v','c')
    return args
    

mudança = escopo_local_legal(args = variavel)
print(mudança) #escopo local
print(variavel) #escopo global"""


# Exemplo 4: 
"""def outro():
    print(variavel) #esse programa da erro justamente porque quando redefino a variavel para 123, a variavel global é desconsiderada e é criada uma variavel local. Como ela foi printada antes de existir, o programa dá um erro. 
    variavel = 123
    print(variavel)
outro()
print(variavel)"""


#Exemplo 5: Acessando variáveis locais a partir de outras variáveis locais. Único método possível.

"""def primeira():
    primeira_var = 'valor2'
    return primeira_var

receber = primeira()
def segunda():
    print(receber)


segunda()"""

#ou

def terceira ():
    outra = 'Valor5000'
    return outra

def quarta(args):
    print(args)
temp_outra = terceira()
quarta(temp_outra)



import re

from click import argument
"04.252.011/0001-10"
"04252011000110"


def valida(argumento):
    tratado = elimina_caracter(argumento)
    sem_digitos = eliminar_digitos_padrao(tratado)
    converte_inteiro = converter_para_inteiro(sem_digitos)
    soma_e_multiplicacao = multiplicacao_e_soma(converte_inteiro)
    def make_cnpj(digito):
        novo_cpf = converte_inteiro
        if digito <= 9:
            novo_cpf.append(digito)
        else:
            novo_cpf.append(0)
        return novo_cpf
    return make_cnpj(primeiro_digito(soma_e_multiplicacao))


    

def number_of_characters(opcao):
    opcao = str(opcao)
    if len(opcao) == 14 or len(opcao) == 18:
        return True
    else:
        return False
   
        
def elimina_caracter(cnpj):
    return re.sub(r"([^0-9])","",cnpj)


def eliminar_digitos_padrao(cnpj_sem_caracter):
    cnpj_sem_d1_d2 = cnpj_sem_caracter[:-2]
    return cnpj_sem_d1_d2


def converter_para_inteiro(sem_digitos):
    converter = [int(v) for v in sem_digitos]
    return converter

    
def multiplicacao_e_soma(convertido_for_int):
    lista1 = [v for v in range(5,1,-1)]
    lista2 = [v for v in range(9,1,-1)]
    juntar = lista1 + lista2
    multi = [x * y for x,y in zip(juntar,convertido_for_int)]
    return sum(multi)


def primeiro_digito(number):
    form = 11 - (number % 11)
    return form

def segundo_digito(number):
    form = 11 - (number % 11)
    return form

while True:
    user = input("Insira: ").strip()
    if number_of_characters(user) == True:
        print(valida(user))
        break
    else:
        print("Número de caracteres inválido! Tente novamente.")

import re
"04.252.011/0001-10"
"04252011000110"


def valida(argumento):
    tratado = elimina_caracter(argumento)
    sem_digitos = eliminar_digitos_padrao(tratado)
    converte_inteiro = converter_para_inteiro(sem_digitos)
    teste = multiplicacao_e_soma(converte_inteiro)
    print(teste)


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


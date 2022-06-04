from itertools import count
import re

"04.252.011/0001-10"
"04252011000110"




def valida(argumento):
    tratado = elimina_caracter(argumento)
    sem_digitos = eliminar_digitos_padrao(tratado)
    return sem_digitos

    


def elimina_caracter(cnpj):

    return re.sub(r"([^0-9])","",cnpj)


def eliminar_digitos_padrao(cnpj_sem_caracter):

    cnpj_sem_d1_d2 = cnpj_sem_caracter[:-2]
    return cnpj_sem_d1_d2




print(valida("04.252.011/0001-10"))
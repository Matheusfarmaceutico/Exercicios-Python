import re
"04.252.011/0001-10"



def validador_cnpj(cnpj_tratado_caracter_digito):
    tratar_carac_digi_local = tratar_caracteres_e_digitos(cnpj_tratado_caracter_digito)
    contagem_numeros = contagem(tratar_carac_digi_local)
    soma_multi = soma_multiplicacao(contagem_numeros)
    

def tratar_caracteres_e_digitos(cnpj_original):
    elimina_carac_especial = re.sub(r"[^0-9]","",cnpj_original)
    def excluir_digitos_verificadores():
        return elimina_carac_especial[:-2]
    return excluir_digitos_verificadores()
        


def contagem(arg):
    
    if len(arg) == 12:
        valores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        return valores
    elif len(arg) == 13:
        valores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        return valores
    return contagem()


def soma_multiplicacao(contagem):
    for c, v in enumerate(contagem):
        tratar_caracteres_e_digitos[c] * v


validador_cnpj("04.252.011/0001-10")
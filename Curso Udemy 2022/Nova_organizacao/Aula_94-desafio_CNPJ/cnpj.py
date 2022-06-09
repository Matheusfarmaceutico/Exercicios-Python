import re
"04.252.011/0001-10"

def validador_cnpj(cnpj_tratado_01):
    print(eliminar_caracteres(cnpj_tratado_01))




def eliminar_caracteres(cnpj_original):
    elimina_carac_especial = re.sub(r"[^0-9]","",cnpj_original)
    def excluir_digitos():
        return elimina_carac_especial[:-2]
    return excluir_digitos()
        



validador_cnpj("04.252.011/0001-10")

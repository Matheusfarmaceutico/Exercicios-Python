
from vendas.calc_preco import aumento,reducao

preco = 49.90

aumento_preco = aumento(valor=preco,porcentagem=15, formata=True)
print(f"{aumento_preco}")


preco_reducao = reducao(valor=preco,porcentagem=30, formata=True)
print(f"{preco_reducao}")



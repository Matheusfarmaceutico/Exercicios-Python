def cadastrar_produtos():
    carrinho = []

    while True:
        produto = str(input("Digite o nome de um produto: "))
        preco = float(input("Digite o valor desse mesmo produto: "))
        option = str(input("Quer continuar? S/N "))
        carrinho.append((produto,preco))
        if option in "Nn":
            break
    return carrinho
def compras(lista):
    total = [(x,y) for x,y in cadastrar_produtos]
    print(total)
#dando erro, continuar tentando amanha

print(compras(cadastrar_produtos))
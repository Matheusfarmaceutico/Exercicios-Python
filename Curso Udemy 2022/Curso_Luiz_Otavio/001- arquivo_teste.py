

def carrinho_compras():
    carrinho = []
    while True: 
        produto = input("Digite o nome do produto:")
        valor = float(input('Digite o valor deste mesmo produto: '))
        carrinho.append((produto,valor))
        option = str(input("Quer continuar? [S/N]: "))
        if option in 'Nn':
            break
    resul = [(y) for x,y in carrinho]
    return sum(resul)


print(carrinho_compras())
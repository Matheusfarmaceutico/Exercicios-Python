carrinho = []
carrinho.append(("melancia",1.89))
carrinho.append(("isopor",2))
total = [(y) for x,y in carrinho]

tot = sum(total)
print(f'{tot:.2f}')


carrinho = []
carrinho.append(("Macarrao",2))
carrinho.append(("Queijo",10))

resultado = [c[1] for c in carrinho]
print(sum(resultado))
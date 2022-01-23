num=[8,2,3,10,24]
num.append(12)
num.sort(reverse=True)
num.insert(3,9)
num.pop()
num.append(3)
#num.remove(3) se o elemento a ser removido já estiver na lista, ele removerá o primeiro que aparece.
print(num)
print(f'Essa lista tem {len(num)} elementos')
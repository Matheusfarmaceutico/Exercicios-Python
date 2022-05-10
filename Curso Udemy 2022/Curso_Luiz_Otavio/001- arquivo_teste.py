from itertools import combinations, permutations, product

pessoas = ["Luiz","André","Eduardo","Letícia", "Fabrício","Rose"]



for p in product(pessoas,repeat = 2):
    print(p)



"""
Combinations, Permutations e Product - Itertools

Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos.
Produto - Ordem importa e repete valores únicos
"""

#Combinations

from itertools import combinations
pessoas = ["Luiz","André","Eduardo","Letícia", "Fabrício","Rose"]
for grupo in combinations(pessoas,2):
    print(grupo)
"""A ordem não importa significa que se eu tiver Eduardo, Rose, não terei Rose,Educardo."""

#permutacions

from itertools import permutations
pessoas = ["Luiz","André","Eduardo","Letícia", "Fabrício","Rose"]
for grupo in permutations(pessoas,2):
    print(grupo)
"""Nesse caso de permutações pode acontecer Eduardo, Rose e Rose e Edurado"""

# Product - Permitem que haja combinações entre o próprio elemento, como Luiz e Luiz

from itertools import product
pessoas = ["Luiz","André","Eduardo","Letícia", "Fabrício","Rose"]
for grupo in product(pessoas,repeat=2):
    print(grupo)

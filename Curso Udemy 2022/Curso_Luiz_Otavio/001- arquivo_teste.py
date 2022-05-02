from itertools import count
from itertools import zip_longest
cidade = ["Sao Paulo", "Goiânia"]
estado = ["SP","GO"]
cont = count()
cidade_estado = zip(cont, estado, cidade)
print(cidade_estado)
for v in cidade_estado:
    print(*v)
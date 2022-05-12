from itertools import groupby, tee


alunos = [
{"Nome":"Matheus","Nota":"A"},
{"Nome":"Luana","Nota":"B"},
{"Nome":"Candida","Nota":"D"},
{"Nome":"Lucas Paquetá","Nota":"B"},
{"Nome":"Isabelao","Nota":"C"},
{"Nome":"Jhonata","Nota":"A"},
 
 
 
 ]


ordena = lambda item: item["Nota"]
alunos.sort(key=ordena)
valores_agrupados = groupby(alunos,ordena)

for agrupamento, db_alunos in valores_agrupados:
    v1, v2 = tee(db_alunos)
    print(f"Agrupamento: {agrupamento}")
    for aluno in v1:
        print(aluno)
    quantidade = len(list(v2))
    print(f"A quantidade de alunos que tiraram nota {agrupamento} foi de {quantidade}")
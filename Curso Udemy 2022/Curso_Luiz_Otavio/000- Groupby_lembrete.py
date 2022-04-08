alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]


def organizar(iter): return iter["nota"]


alunos_ordenados = sorted(alunos, key=organizar)
grupos_separados = groupby(alunos_ordenados, organizar)

for agrupamentos, full_dados in grupos_separados:
    print()
    print(f"Agrupamentos {agrupamentos}")
    # trata-se de um iterador que se esgota, por isso tee faz duas cópias de "full dados", para que eu consiga exibir os nomes dos alunos e a quantidade deles que tiraram uma determinada nota"
    v1, v2 = tee(full_dados)

    for aluno in v1:
        # V1 é uma cópia de full_dados, e a utilizo aqui para que eu possa exibir o nome do aluno daquele grupamento em específico.
        print(aluno["Nome"])
    # V2 é uma cópia de full_dados, e a utilizo aqui para quantificar quantos alunos estão em um determinado grupamento de notas. Note que preciso v2 (que é um objeto) para uma lista, para que eu quantificar antes de exibir o len, de fato.
    quantidade = len(list(v2))
    print(f"Quantidade de alunos do agrupamento {agrupamentos}:  {quantidade}")

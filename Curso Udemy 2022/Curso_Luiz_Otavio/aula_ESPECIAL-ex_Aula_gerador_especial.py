
#Utilizando listas normais, sem geradores.
from timeit import timeit


matriculados= ["Matheus","Ana","Yara","Joana"]
opcao_curso = ["Farmácia","História","Biologia","Física"]
def cadastro(nome,curso):
    dados = []
    for i,(nome,curso) in enumerate(zip(nome,curso)):
        aluno = {
            "Matrícula": i,
            "Nome":nome,
            "Curso":curso
        }
        dados.append(aluno)
    return dados


for v in cadastro(matriculados,opcao_curso):
    print(v)

print("-="*30)

#utilizando geradores


def gerador (nome,curso):
    for i,(nome,curso) in enumerate(zip(nome,curso)):
        alunos = {
            "ID":i,
            "Aluno":nome,
            "Curso":curso
        }
        yield alunos


g = gerador(matriculados,opcao_curso)
for v in g:
    print(v)


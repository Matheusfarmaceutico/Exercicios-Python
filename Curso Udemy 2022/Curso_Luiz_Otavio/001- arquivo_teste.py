matriculados= ["Matheus","Ana","Yara","Joana"]
opcao_curso = ["Farmácia","História","Biologia","Física"]







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
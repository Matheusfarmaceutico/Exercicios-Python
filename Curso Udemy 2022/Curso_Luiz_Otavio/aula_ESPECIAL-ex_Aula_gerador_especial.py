
#Utilizando listas normais, sem geradores.
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


print(cadastro(matriculados,opcao_curso))
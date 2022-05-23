import os

try:
    os.remove("Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/teste.txt")
except:
    pass
cmd = "git status  ."

chamada = os.system(cmd)
print(chamada)
try:
    os.rename(src="/home/matheus/Documentos/Repositorios_Linux/Exercicios-Python/Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/velho.txt",dst="/home/matheus/Documentos/Repositorios_Linux/Exercicios-Python/Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/novo.txt")
except:
    pass




#consigo mover um arquivo com os.rename

origin = "/home/matheus/Documentos/Repositorios_Linux/Exercicios-Python/Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/movendo.txt"

destiny = "/home/matheus/Documentos/Repositorios_Linux/Exercicios-Python/Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/movendo/movendo.txt"
try:
    os.rename(origin,destiny)
except:
    print("Codigo já executado e arquivo já movido")
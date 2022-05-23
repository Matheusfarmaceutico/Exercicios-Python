from itertools import count

# atualiza o arquivo anterior com também os nomes (append mode)

with open("Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando.py/nomes-cpf.txt","a+") as file:
    file.write("Matheus\n")
    file.write("Ricardo\n")
    file.write("Henrique\n")
   

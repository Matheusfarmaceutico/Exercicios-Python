# Maneira tradicional de se lidar com arquivos, muito utiliza em outras linguagens de programação
try: 
    file = open("/home/matheus/Documentos/Repositorios_Linux/Exercicios-Python/Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando.py/abc.txt","w+")
    file.write("Teste")
    file.seek(0,0)
    print(file.read())
finally:
    file.close()

# Maneira pythonica, mais adequada, utilizando gerenciador de contexto Python

with open("/home/matheus/Documentos/Repositorios_Linux/Exercicios-Python/Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando.py/contexto.txt","w+") as file:
    file.write("Linha01\n")
    file.write("Linha02\n")
    file.write("Linha03\n")
    file.seek(0,0)
    print(file.read())


''' NO caso acima, o gerenciador de contexto automaticamente fecha o arquivo, n havendo a necessidade de fazer file.close()
'''
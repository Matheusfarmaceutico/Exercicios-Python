

file = open("/home/matheus/Documentos/Repositorios_Linux/Exercicios-Python/Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando.py/abc.txt","w+") # w = escrita; + permite leitura e escrita
file.write("Linha 01 \n")
file.write("Linha 02 \n")
file.write("Linha 03 \n")
file.write("Linha 04 \n")
file.write("Linha 05 \n")
file.seek(0,0) # O primeiro par me permite configurar a partir de qual caracter ele vai ler
print("Lendo Linhas")
print(file.read()) #preciso fazer o seek para resetar o cursor de leitura

print("-="*30)
print("Ler linha por linha")

file.seek(0,0)
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(next(file),end="") # percebi que funciona como um iterador

print("-="*30)
print("Salvando as linhas em um dicionáriio")
file.seek(0,0)

print(file.readlines())
file.seek(0,0)
for linha in file.readlines():
    print(linha,end="")
file.seek(0,0)

for linha in file:
    print(linha,end="")
file.close()



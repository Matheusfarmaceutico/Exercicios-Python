import json


with open("Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/first_js.json","r") as file:
    
    json_file = file.read()
    print(json_file)


with open("Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/second_js.json","w+") as file:
    file.write(json_file)
    
    json_file = json.loads(json_file) # loads me permite retranformar para dicionário
    print(json_file['pessoa 1'])

    

import json

d1 = {
    "pessoa 1": {
        "nome":"Luiz",
        "idade": 34,
    },
    "pessoa 2": {
        "nome":"Maria",
        "idade": 27,
    }
}


d1_json = json.dumps(d1,indent=True)


with open("Curso Udemy 2022/Nova_organizacao/aula_89_criando-lendo-escrevendo-apagando/first_js.json","w+") as file:
    
    file.write(d1_json)


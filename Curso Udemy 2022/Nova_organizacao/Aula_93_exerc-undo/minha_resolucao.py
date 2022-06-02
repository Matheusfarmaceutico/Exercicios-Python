

# CHECAR GITHUB PARA VER ESTE MESMO CÓDIGO REFEITO COM VARIÁVEIS EM PORTUGUES PARA FÁCIL ENTENDIMENTO!!!!!
"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa"""



def show_up(to_do_list):
    print("-="*30)
    print("Tarefas: ")
    print(to_do_list)
    print("-="*30)


def do_add(option, to_do_list):
    to_do_list.append(option)


def do_undo(to_do_list,re_list):
    if  not to_do_list:
        print("Nada a desfazer")
        return
    last_to_do = to_do_list.pop()
    re_list.append(last_to_do)
    print(f"{last_to_do} foi eliminado da lista.")

def do_redo(to_do_list, re_list):
    if not re_list:
        print("Nada a refazer!")
        return
    last_re_list = re_list.pop()
    to_do_list.append(last_re_list)
    print(f"{last_re_list} foi reposto na lista")
    
if __name__ == "__main__":
    to_do_list = []
    re_list = []

    while True:
        option = str(input("Digite uma tarefa ou undo, rendo e ls: "))

        if option == "ls":
            show_up(to_do_list)
            continue
        elif option == "undo":
            do_undo(to_do_list,re_list)
            continue
        elif option == "redo":
            do_redo(to_do_list,re_list)
            continue
        do_add(option, to_do_list)
    
        




#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort() No final, mostre a lista ordenada na tela.

def number_in_correct_position():
    inserted_numbers = []
    for c in range(0,5):
        user_values = int(input(f'Entered a valid {c + 1}º number:  '))
        if c == 0 or user_values >= inserted_numbers[-1]:
            inserted_numbers.append(user_values)

        else:
            for key, value in enumerate(inserted_numbers):
                if user_values <= value:
                    inserted_numbers.insert(key,user_values)
                    break

    print(inserted_numbers)
number_in_correct_position()
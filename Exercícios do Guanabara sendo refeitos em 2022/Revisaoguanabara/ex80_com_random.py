#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort() No final, mostre a lista ordenada na tela.
from random import randint

def number_in_correct_position():
    inserted_numbers = []
    print("Original Values generated in the following sequence: ",end= '')
    for c in range(0,5):
        user_values = randint(1,1000)
        if c != 4:
            print(user_values,end= ',')
        else:
            print(user_values,end='.')


        if c == 0 or user_values >= inserted_numbers[-1]:
            inserted_numbers.append(user_values)

        else:
            for key, value in enumerate(inserted_numbers):
                if user_values <= value:
                    inserted_numbers.insert(key,user_values)
                    break
    print()
    print(inserted_numbers)
number_in_correct_position()
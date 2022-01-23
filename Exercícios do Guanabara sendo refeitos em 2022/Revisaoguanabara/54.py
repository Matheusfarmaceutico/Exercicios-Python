"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date
under_age = 0
of_age = 0
actual_year = date.today().year
for year in range(1, 8):
    rising = int(input(f'{year} person, please, enter a valid year of birth: '))
    if actual_year - rising < 18:
        under_age += 1
    else:
        of_age += 1
print(f'We had {under_age} minors and {of_age} of age. ')
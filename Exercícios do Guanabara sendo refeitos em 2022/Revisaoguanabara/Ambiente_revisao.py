#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 






def major_and_minor():
    numbers = []
    major_value = minor_value = 0
    cont = 0
    while cont < 5:
        try:
            numbers.append(int(input(f'Enter a valid {cont + 1}º number: ')))
            cont += 1
        except:
            print("Invalid character! Try again.")
            continue
    for k, v in enumerate(numbers):
        if k == 0:
            major_value = minor_value = v
        else:
            if v > major_value:
                major_value = v
            if v < minor_value:
                minor_value = v
    return {"Major value": major_value, "Minor value":minor_value}
answers = major_and_minor()
print(answers)
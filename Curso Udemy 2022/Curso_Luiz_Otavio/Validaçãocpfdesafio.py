"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# o intuito desse procedimento é gerar dois dígitos de cpf finais de acordo com os 8 disponíveis.
# Se o cpf inserido pelo usuário ou pela string não for compatível com o número inteiro + dígitos gerados
# entao o cpf é falso. Há uma lógica matemática que gera os dois dígitos finais de acordo com os antecessores.
cpf = '70374405157'  # cpf original com dígitos verificadores
novo_cpf = cpf[:-2]  # cpf sem os dois últimos dígitos verificadores.
reverso = 10  # inicia contagem do reverso
total = 0  # recebe o resultado de cada laço, multiplicação de dígito por reverso
for index in range(19):  # Gerar 1 e 2 dígitos. novo_cpf[index] dispõe 9 p digitos pra gerar o 1, e depois os 10
    # outros para gerar o 2. Inverso tmb tem a mesma função, começando com contador em 10 para o 1, e 11 para o 2.
    if index > 8:  # Separar a geração do 1 e do 2 termo.Cont. recomeça.
        index -= 9
    total += int(novo_cpf[index]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11
        digitos = 11 - (total % 11)
        if digitos > 9:
            digitos = 0
        total = 0
        novo_cpf += str(digitos)

if cpf == novo_cpf:
    print('CPF VÁLIDO')
else:
    print('inválido')

#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
tot=quant=menor=cont=0
nomeproduto=''
while True:
    produto=str(input('Digite o nome do produto:')).strip()
    preço=float(input('Digite o preço do produto R$'))
    cont+=1
    tot+=preço
    if preço>1000:
        quant+=1
    if cont==1 or preço<menor:
        menor=preço
        nomeproduto=produto
    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp=='N':
        break
print('==== FIM DO PROGRAMA! ====')
print("O total da compra foi de R${:.2f}".format(tot))
print(F'{quant} produtos custam mais do que R$1000')
print(f'O produto mais barato é o(a){nomeproduto}, que custa R${menor:.2f}')


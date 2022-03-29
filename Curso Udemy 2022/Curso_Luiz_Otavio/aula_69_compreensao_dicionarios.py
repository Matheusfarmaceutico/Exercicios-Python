#O funcionamento de compreensao de listas e dicionários é semelhante.



#posso converter uma list comprehension em dictionary comprehension
lista= [("chave","valor"),]
d1 = dict([(y, x * 2) for x,y in lista])
print(d1)
print()

#como também posso fazer um dictionary comprehension diretamente

lista = [("chave","valor"),]
d2 = {x:y * 2 for x,y in lista}
print(d2)
print()
#posso fazer sets comprehension


set_01 = {x for x in range(0,5)}
print(set_01)
print()
#posso preencher chaves e valores com dictionary comprehension

gerar = {f'chave_{x}':y for x,y in enumerate(range(0,5)) } #note que utilizei o enumerate para conseguir fazer o range nos dois valores. Se que quisesse apenas utilizar o range para modificar a chave, bastava utilizar apenas o range.
print(gerar)

l=float(input('Qual a largura da parede?'))
a=float(input('Qual a altura da parede?'))
ar=l*a
print('Sua parede tem dimensões de {}x{} e sua área é de {}m²'.format(l,a,ar))
print('Para pintar a parede, você precisará de {}l de tinta.'.format(ar/2))
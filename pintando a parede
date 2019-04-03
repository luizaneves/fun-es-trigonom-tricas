larg = float(input('Qual a largura da sua parede?'))
alt = float(input('Qual a altura da sua parede?'))

area = larg * alt

t = area/2
lata = t/18
preço_lata = 160.00
if lata < 1:
    lata = 1
    print('Você pode compra só uma lata que sera suficiente para pintar sua parede')
else:
    lata = lata
    print('você vai precisar de {} latas de tinta para pintar sua parede'.format(lata))


print('Sua parede tem {} metros quadrados'.format(area), end=' e ')
print('Voçê ira precisar de {} litros de tinta para pintar toda a sua parede'.format(t))
print('O preço da lata de tinta é R${}'.format(preço_lata))
res = str(input('O senhor vai levar a tinta ?'))
if res == 'sim':
     total_pagar = lata * preço_lata
     print('O seu orçamento vai ficar em R${}'.format(total_pagar))
else:
    print('Que pena :/')

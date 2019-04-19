from time import sleep
print('-*-' * 18)
print('Vamos analisar um triângulo:')
print('-*-' * 18)
sleep(0.5)

s1 = float(input('Digite o valor do primeiro segmento:'))

s2 = float(input('Digite o valor do segundo segmento:'))

s3 = float(input('Digite o valor do terceiro segmento:'))

if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3> s2:
    print('Com essas medidas de segmentos é possível formar um triângulo!')
else:
    print('Com essas medidas de segmentos NÃO é possível formar um triângulo!')

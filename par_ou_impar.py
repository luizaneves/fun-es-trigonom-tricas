from time import sleep
print('Vamos aprender a descobrir se um número é par ou ímpar')
sleep(1)
num = int(input('Digite um número qualquer:'))
res = num % 2
if res == 0:
    print('Este número é par!')
else:
    print('Este número é ímpar!')

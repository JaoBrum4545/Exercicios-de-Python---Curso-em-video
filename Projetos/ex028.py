from random import randint
n = int(input("insira um numero de 1 à 6: "))
x = randint(1,6)
print('O número foi: {}!'.format(x))
#if n == x:
#    print('Você acertou!')
#else:
#    print('Você errou!')

print('Você acertou!'if n == x else 'Você errou!')
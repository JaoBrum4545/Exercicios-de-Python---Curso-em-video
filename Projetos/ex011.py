import math
n1 = float(input('Insira a altura: '))
n2 = float(input('Insira a largura: '))
tam = n1*n2
print("A quantidade de tinta que precisa para pintar {} é de {} baldes".format(tam,math.ceil(tam/2)))

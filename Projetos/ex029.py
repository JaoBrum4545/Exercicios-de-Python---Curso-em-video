n = float(input('Entre com a sua velocidade: '))
if n > 80:
    print('MULTADO!\nVocê deve pagar R${:.2f}!'.format((n-80)*7))
else :
    print('okok!')
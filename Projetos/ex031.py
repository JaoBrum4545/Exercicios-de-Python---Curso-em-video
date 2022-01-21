dis = float(input('Insira a distância: '))
print('Custo: R${:.2f}!'.format(dis*0.5) if dis<200 else 'Custo: R${:.2f}!'.format(dis*0.45))
ano = int(input('Insira um ano: '))
if ano != 0:
    if((ano%100==0)and(ano%400!=0)):
        print('{} não é bissexto!'.format(ano))
    else :
        print('{} é bissexto!'.format(ano))
else :
    print('{} não é bissexto!'.format(2017))
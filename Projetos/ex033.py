n1 = int ( input ("1°: ") )
menor = n1
maior = n1
n2 = int ( input ("2°: ") )
if maior < n2 :
    maior = n2
if menor > n2 :
    menor = n2
n3 = int ( input ("3°: ") )
if maior < n3 :
    maior = n3
if menor > n3 :
   menor = n3
print ("Maior: {}\nMenor: {}".format(maior,menor))
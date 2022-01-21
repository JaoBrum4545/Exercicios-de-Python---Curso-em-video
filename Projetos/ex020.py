from random import shuffle
str1 = str(input("n1: "))
str2 = str(input("n2: "))
str3 = str(input("n3: "))
str4 = str(input("n4: "))
lista = [str1,str2,str3,str4]
shuffle(lista)
print("Sequencia: ",lista)
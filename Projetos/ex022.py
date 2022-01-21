nome = str(input("Insira seu nome: ")).strip()
print("Seu nome em letras maiúsculas: {}.".format(nome.upper()))
print("Seu nome em letras minúsculas: {}.".format(nome.lower()))
lista = nome.split()
print("Seu nome tem {} letras!".format(len(nome)-nome.count(' ')))
print("Seu primeiro nome é {}, e ele tem {} letras!".format(lista[0],len(lista[0])))
#João Pedro Brum Terra
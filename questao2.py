lista1 = [5,3,1,2]
lista2 = [5,2,4,1]
lista3 = []

for elemento in lista1:
    lista3.append(elemento)

for elemento in lista2:
    lista3.append(elemento)

for x in range(len(lista3)):
    print(f"ELEMENTO {x} : {lista3[x]}")
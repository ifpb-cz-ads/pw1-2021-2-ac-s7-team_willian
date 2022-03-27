lista1 = [2,4,6,1]
lista2 = [3,5,6,2]
combined = [lista1, lista2]
union = list(set().union(*combined))
print(union);
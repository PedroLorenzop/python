lista = [23, 54, 65 ,423, 321 ,53, 132]
for i in range(len(lista))
aux = lista[i]
j = i -1
print(lista)
while lista[j] > aux and j >= 0:
    lista[j + 1] = lista[j]
    j = j -1
    print(lista)

lista[j + 1] = aux
print(lista)



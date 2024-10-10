lista = [1, 3, 65, 23, 6, 9]

partida = 1


def minElemento(partida, lista):
    min= partida
    for i in range(partida + 1, len(lista)):
        if lista[min] > lista[i]:
            min = i
    return min

for j in range(len(lista)):
    menor = minElemento(j,lista)
    aux = lista[menor]
    lista[menor] = lista[j]
    lista[j] = aux
print(lista)
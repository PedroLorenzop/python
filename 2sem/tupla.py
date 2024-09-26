listas = [1, 2, 3]
tupla = (1, 2 ,3)

print(listas)
print(tupla, type(tupla))


addTupla = tuple([])

for i in range(1, 10):
    addTupla += (i,)
print(addTupla)

remoTupla = (1, 2, 3, 4, 5)
remoTupla = list(remoTupla)

rem = 3
for i, j in enumerate(remoTupla):
    if j == rem:
        remoTupla.pop(i)
print(tuple(remoTupla))
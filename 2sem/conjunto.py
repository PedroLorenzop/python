'''
a = set([1, 2, 3, 4]) #declaracao de conjunto
b = {1, 2, 3, 4, 5, 6} #outra forma de declarar conjunto
print(a)

a.add(5) #adiciona um elemento ao conjunto

#uniao
c = a | b
#diferenca
d = a - b

#interseção
e = a & b

print(c)
print(d)
print(e)
'''

f = set([1, 2, 3, 4, 5, 9])
g = set([1, 2, 3, 4, 5, 6 ,7])


#intersecao
h = f & g
print(f"interseccao {list(h)}")

#diferenca do primeiro set
i = f - g
print(f"diferenca {list(i)}")

#diferenca do segundo set
j = g - f
print(f"diferenca {list(j)}")

#valores nao repetidos
k = f ^ g  #tbm pode ser feito dessa maneira (k = i | j)
print(f"Valores nao repetidos {list(k)}")
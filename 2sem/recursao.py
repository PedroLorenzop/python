#soma de lista sem for ou while

'''
l = [1, 3, 5, 7]

def soma(l):
    if len(l) == 1:
        return l[0]
    return l[0] + soma(l{1:})

print(soma(l))


#soma fatorial
fat = 4
def fatorial(fat):
    if fat == 0:
        return 1
    return fat * fatorial(fat - 1)

print(fatorial(fat))



#fibonacci

f = 2
def fibo(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    return (fibo(f - 1) + fibo(f -2))
        
print(fibo(f))




def potencia(pot, n):
    if pot == 0:
        return 1
    elif pot == 1:
        return n
    return n * potencia(pot - 1, n)

pot = 2
n = 10

print(potencia(pot, n))



#combinacao

def combinacao(m, n):
    if n == 0 or m == n:
        return 1
    elif m > n and m > 0 and n > 0:
        return (m - 1 + n) + (m - 1 + n - 1)
    return 
    
print(combinacao(1, 2))
'''

def expo()
#ex1
def compra(lista_de_compras,supermercado):
    valor = 0
    contem = []
    nao_contem = []
    for i in lista_de_compras:
        if i in supermercado:
            valor += supermercado[i]
            contem.append(i)
        else:
            nao_contem.append(i)
    return valor, contem, nao_contem

#ex2
def ordena(a):
    for iter in range(len(a)-1,0,-1):
        for i in range(len(a)-1):
            if a[i][1] > a[i+1][1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
    return a

#ex3
def busca_sequencial(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return -1

#ex4
def atual_estoque(estoque_atual, novos_itens):
    for i in novos_itens.keys():
        if i in estoque_atual:
            estoque_atual[i] += novos_itens[i]
        else:
            estoque_atual[i] = novos_itens[i]
    return estoque_atual
#ex5
def medalhas_pais(olimpiadas, pais):
    for i in olimpiadas['data']:
        if i['name']==pais:
            return (i['name'], i['total_medals'], i['gold_medals'], i['silver_medals'], i['bronze_medals'])

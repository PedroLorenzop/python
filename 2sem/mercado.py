lista_de_compras = ["biscoito", "chocolate", "farinha"]


supermercado = {
    "amaciante":4.99,
    "arroz":10.90,
    "biscoito":1.69,
    "cafe":6.98,
    "chocolate":3.79,	
    "farinha":2.99
}



valor = 0
for i in lista_de_compras:
    if i in supermercado:
        valor += supermercado[i]
    else:
        print(f"Produto {i} não encontrado no supermercado.")
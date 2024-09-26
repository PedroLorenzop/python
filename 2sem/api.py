import requests
'''
cep = input("Digite seu cep: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

r = requests.get(url)
info = r.json()

print(f"Rua: {info['logradouro']}, Bairro: {info['bairro']}, Cidade: {info['localidade']} e estado: {info['estado']}.")
'''

url = "https://pokeapi.co/api/v2/pokemon/eevee"

r = requests.get(url)
info = r.json()



#Mostrar o id do pokemon e o tipo dele
print(f"{info['id']}, {info['types'][0]['type']['name']}")



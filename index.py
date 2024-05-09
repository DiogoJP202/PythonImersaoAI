import requests # Requisitei a biblioteca para utilizar APIs.
import random # Utilizei a biblioteca para usar a funções de escolhas aleatórias.

# Guardando o valor da url em uma variável. A url é uma API.
url = "https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json"
# Utilizando a biblioteca para capturar o valor da API. 
resposta = requests.get(url)

# Transformando o valor em JSON.
data = resposta.json()

# Verifica a quantidade de valores dentro de um array.
len(data)

# Imprimindo o valor do primeiro array da variável data
print(data[0])
print("--------")

# Utilizou a biblioteca que realiza uma função de escolha aleatória.
valor_secreto = random.choice(data)

# Selecionando a chave "palavra" do objeto.
palavra_secreta = valor_secreto["palavra"]

# Selecionando a chave "dica" do objeto.
dica = valor_secreto["dica"]

# Imprimindo a quantidade de elementos (chaves) da variável "palavra_secreta"
print(len(palavra_secreta))
print("--------")
print(dica)
print("--------")
# "f" junta um texto com valores ou variáveis
print(f"A palavra secreta tem {len(palavra_secreta)} letras -> {dica}")
print("--------")

# Input do usuário, recebe a mensagem do terminal.
restoposta = input(f"A palavra secreta tem {len(palavra_secreta)} letras -> {dica}")

# Criando condições.
if(resposta == palavra_secreta):
    print(f"A resposta está certa, a palavra era {palavra_secreta}!")
else:
    print(f"A respota está errada, a palavra era {palavra_secreta}!")
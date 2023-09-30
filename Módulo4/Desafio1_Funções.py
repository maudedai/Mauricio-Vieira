# DESAFIO 1 - 
# Crie uma função chamada gerar_nome_completo que recebe como parâmetro
# o nome e sobrenome de alguém e dá boas vindas para essa pessoa

def gerar_nome(sobrenome, nome):
    print(f"Bem-vindo {nome} {sobrenome}")

gerar_nome("de Souza Vieira", "Maurício")

# DESAFIO 2 - 
# # Crie uma função chamada calcular_valores que recebe 2 parâmetros 
# o primeiro o preco de um produto e o segundo parâmetro é a quantidade, 
# porém a quantidade deve haver um valor padrão de 1. 
# Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.

def calcular_valores(preco, quantidade=1):
    print(f"Preço do produto: R${preco * quantidade}")

calcular_valores(2.5, 2)    
# Valores aleatórios com random
import random

print(random.random()) #Gera um valor de 0.0 a 1.0 Gera um valor decimal de valor mínimo ao valor máximo
print(random.uniform(4, 10)) #Gera valores tanto inteiros quanto decimais
print(random.randint(0, 100))

cores = ['verde', 'vermelho', 'amarelo']
print(random.choice(cores)) #Seleciona aleatóriamente uma das opções contidas dentro da variável (lista) cores
print(random.choices(cores, k=2)) #Com a opção 'k', é possível inserir a quantidade de itens a serem exibidos dentro da amostragem

#para embaralhar valores de uma lista
cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)
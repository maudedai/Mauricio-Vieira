# O for é iniciado com uma variável do tipo int, onde o nome dessa variável não importa, ela é apenas usada para iniciar o contador que será limitado no RANGE
for numero in range(5):
    print('carro', numero)

# no caso abaixo, a variável 'nome', está no singular pois siginifica a posição de cada nome dentro da lista 'nomes', ou seja,
# quando eu ponho o loop for nome in nomes, eu vou buscar o nome na posição 0, o nome da posição 1 e assim por diante... 
nomes = ['Maurício', 'Daiana', 'Pedro', 'Aline']
for nome in nomes:
    print(nome)
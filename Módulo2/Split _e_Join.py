frase = 'Olá, bem-vindo a este treinamento'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'Maurício, Daiana, Pedro, Aline'
print(nomes.split())
print(nomes.split(','))
hashtags = 'music #guitar #gamer #coder #pyhton'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
# Como concatenar(combinar) strings
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))
# Continue tem a função de ignorar / pular
for numero in range (100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue
for numero in range (100):
    if numero % 2 == 0:
        print(numero)
    else:
        break

frutas = ['Maçã', 'Manga', 'Laranja', 'Morango']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    else:
        print(f'{fruta} adicionada a dieta')
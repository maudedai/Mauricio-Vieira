celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']

versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']
# imprima na tela a marca + celular de todos celulares, usando as informações acima

for celular in celulares:
    for versao in versoes:
        print(f'{celular} {versao}')
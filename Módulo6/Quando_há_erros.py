    # Exceções
while True:
    try:
        valor = int(input("Digite um valor em dólares: "))
        print(valor * 5.25)
        break
    except:
        print("Digite apenas números!")    
try:
    valor = int(input("Digite um valor: "))
    print(valor / 0)
except ZeroDivisionError as erro:
    print("Não é possível dividir um número por zero!")
except ValueError as erro:
    print("Digite apenas números!")
finally:
    print("A operação foi cancelada")
    # O bloco FINALLY irá realizar um determinado comando
    # mesmo que um problema anterior seja relatado
    # para evitar erros futuros
# from datetime import datetime

# def depositar_dinheiro():
#     print("Depositando dinheiro")

#     def depositando_dolar():
#         print("Depositando dolares")

#     def depositando_reais():
#         print("Depositando reais")

#     depositando_dolar()
#     depositando_reais()

# depositar_dinheiro()

# def pai(numero):
#     def filho_1():
#         print("Sou o filho 1")
#     def filho_2():
#         print("Sou o filho 2")
#     if numero == 1:
#         return filho_1
    
# resultado = pai(1)
# resultado()

# Decorator
def meu_decorator(funcao):
    def decorador():
        print("Antes")
        funcao()
        print("Depois")
    return decorador

'''Ou posso colocar a informação '@meu_decorador' para reduzir
a quantidade de linhas para obter um retorno da função parabenizar(),
ou posso utilizar as linhas comentadas abaixo, porém devo
remover a linha que contém 'parabenizar()'''
@meu_decorator
def parabenizar():
    print("Parabens!!")
parabenizar()

#Resultado = meu_decorator(parabenizar)
#Resultado()
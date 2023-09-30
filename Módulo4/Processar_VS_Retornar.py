 # Processar VS Retornar
# Função que apenas processa dados
print("Olá")
 #funções que retornam dados
cidade = input("Qual a sua cidade? ")

''' Como escolher entre funções que precessam VS Retornam dados?
Eu vou precisar de usar essa informaçã na lógica do meu programa ainda?
ou só preciso processar esse dado, e não irei utilizar mais ele depois?
No primeiro caso é utlizado o RETURN, para o segundo, que é o mais indicado
de ser utilizado, utiliza-se o método PRINT, por exemplo.'''

# asdf


def exibir_cotacao_do_dia(moeda):
    if moeda == "usd":
        return 6.47

cotacao = exibir_cotacao_do_dia("usd")
if cotacao > 5:
    print("Investir em ações americanas")
else:
    print("Cotação não favorável")
def exibir_preco(nome_produto, preco):
    print(f"{nome_produto} está custando o valor de: {preco}")

# Argumentos posicionais

#exibir_preco("Iphone", 5000)
exibir_preco(nome_produto="Iphone", preco=5000)

# Argumentos nomeados
exibir_preco(preco=5000, nome_produto="Iphone")

'''Ao colocar o síbolo de asterisco ('*') na frente de 
um argumento, todos os argumentos após o asteriscor passarão
a ser argumentos nomeados, enquanto o que estiver a frente
serão argumentos posicionais. Exemplos baixo'''

def exibir_preco(nome_produto, *, preco):
    print(f"{nome_produto} está custando o valor de: {preco}")

def exibir_preco(*, nome_produto, preco):
    print(f"{nome_produto} está custando o valor de: {preco}")

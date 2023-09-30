# Tuplas são listas que não podem ter seus valores alterados,
# Sejam para mais ou para menos
# para evitar programações como:

site1 = 'youtube.com'
site2 = 'facebook.com'
site3 = 'instagram.com'
# ou
valor1 = 23
valor2 = 43
valor3 = 65

# Criação da Tupla
sites = ("youtube.com", "facebook.com", "instagram.com")

valores = (23, 43, 65)
print(sites[1])
print(valores[1])

# União de Tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)
print(dados_do_sistema[2])
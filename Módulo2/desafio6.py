'''DESAFIOS
DESAFIO 1: ENCONTRE O ÍNDICE DE 'O' DENTRO DA VARIÁVEL BIBLIOTECA'''
biblioteca = 'biblioteca'
# Gerei o código retornoando a letra 'O' print(biblioteca[biblioteca.rindex('o')])

#OU

# Gerei o código retornoando a letra 'O' print(biblioteca[5])

#OU

print(biblioteca.index('o'))

''''DESAFIO 2
USANDO A FRASE 'DESENVOLVIMENTO DE APLICAÇÕES' IMPRIMA APENAS:
'DE APLICAÇÕES' '''

dda = 'Desenvolvimento De Aplicações'
print(dda.rindex('D'))
print(dda[16:])
print(dda[-13:])

#ou

indice_d = dda.rindex('D')
indice_s = dda.rindex('s')
print(dda[indice_d:indice_s+1]) #forma mais inteligente e limpa de se fazer
teclado = 'TecladoTecladoTecladoTecladoTeclados'
print(teclado[2])
print(teclado[4])
print(teclado[-1])
print(teclado.index('l'))
print(teclado[teclado.index('l')]) #Buscando dinâmicamente um string

#Acessando partes de um string
link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
# print(link[:-5])

#Acessando o último caracter de uma ocorrência / frase que esteja repitido
frase = 'Clean Code'
print(frase.rindex('C'))
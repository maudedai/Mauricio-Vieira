'''DESAFIOS
DESAFIO 1
​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
TRANFORME A FRASE 1 EM UMA LISTA DE PALABRAS E GARDE O RESULTADO EM 
UMA VARIÁVEL CHAVADA PALAVRAS1'''
frase1 = 'Desafio manipulação de strings'
palavras1 = frase1.split()
print(palavras1)

'''DESAFIO 2
Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
TRASNFORME A FRASE 2 EM UMA LISTA DE PALAVRAS E GUARDE O RESULTADO
EM UMA VARIÁVEL CHAVADA PALAVRAS2'''
frase2 = 'jhonatan,rafael,carol,camilla'
palavras2 = frase2.split(',')
print(palavras2)

'''DESAFIO 3
Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
PEGUE O PALAVRAS1 E TRANSFORME ELAS NO SEGUINTE STRING: "DESAFIO,
MANIPULAÇÃO,DE,STRINGS". IMPRIMA O RESULTADO NO CONSOLE'''
palavras3 = ','.join(palavras1)
print(palavras3)

''''DESAFIO 4
Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.
PEGUE O PALAVRAS2 E TRANSFORME ELAS NO SEGUINTE STRING: FRASE2 =
"JHONATAN & RAFAEL & CAROL & CAMILLA". IMPRIMA O RESULTADO NO CONSEOLE'''
print(' & '.join(palavras2))
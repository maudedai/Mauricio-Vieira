''' Crie uma função chamanda gerar_objeto_personalizado que irá
receber 3 parâmetros, cor, altura e formato. A sua função deve 
apenas imprimir na ttela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras:

1- O primeiro argumento deve ser posicional;
2- O 2º e 3º argumentos devem ser OBRIGATÓRIAMENTE nomeados'''

def gerar_objeto_personalizado(cor, *, altura, formato):
    print(cor, altura, formato)

gerar_objeto_personalizado('azul', altura=1.88, formato='quadrado')
''' Quando queremos receber uma variedade infinita de argumentos nomeados
colocamos os asteriscos duplos, e chamamos de Kwargs que significam
Keyword arguments'''

def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nś', b='Somos', c='Pythonistas', d='Profissionais')

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)

fazer_calculo('Mau', 4, 5, 6, 7, 8, a=1, b=2, c=5, d=5)
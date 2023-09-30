# Conversão de tipos

# idade = input('Qual a sua idade? ')
# print(idade > 18)
# TypeError: '>' not supported between instances of 'str' and 'int'

idade = int(input('Qual a sua idade? '))
print(idade > 18)

altura_da_parede = float(input('Qual a altura da parede? '))
print(altura_da_parede > 2.10)
# ou pode ser resolvido também da seguinte forma
altura_da_parede = input('Qual a altura da parede? ')
print(float(altura_da_parede) > 2.1)
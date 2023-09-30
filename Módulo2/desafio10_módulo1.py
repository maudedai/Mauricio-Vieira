## PROJETO 1 

## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1
'''

1. Obtenha o nome do usuário
'''
from datetime import datetime
from datetime import date
import random
# nome = input('Digite o seu nome: ')
# #2. Obtenha a idade do usuário
# data_nascimento = datetime.strptime(input('Digite a sua data de nascimento: '), '%d/%m/%Y')
# #idade = int(input('Digite sua idade: '))
# #3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
# data_cadastro = datetime.today()
# #4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
# cartoes = ['R$50,00','R$250,00','R$120,00']

# #5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
# idade = data_cadastro - data_nascimento
# # print(data_nascimento, data_cadastro, idade)
'''Módulo 2 - Gerar apresentação do usuário

# Funcionalidades do módulo 2 - Mensagem de boas vindas!
Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).

Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).'''
# # print(f'\nOlá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {random.choice(cartoes)}.')

print('----------Olá, bem-vindo a nossa empresa-----------')
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
data_cadastr0 = datetime.now()
cartoes = ['R$50,00','R$250,00','R$120,00']
cartao = random.choice(cartoes)
aniversario = datetime.strptime(input('Digite a sua data de nascimento no formato dd/mm/aaaa: '), '%d/%m/%Y')
print(f'\nOlá {nome}, seu registro foi concluído com sucesso no dia: {data_cadastr0.day}/{data_cadastr0.month}/{data_cadastr0.year}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}.')
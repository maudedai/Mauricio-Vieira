# Funcções
# input()
# len()
# split()

'''modelo de função def
def nome_da_função(parametros):
    comando
    '''
# def dar_boas_vindas():
#     print("Bem-Vindo!")

# dar_boas_vindas()

# def dar_boas_vindas_personalizadas(nome):
#     print(f"Bem-Vindo(a) {nome}")

# dar_boas_vindas_personalizadas("Maurício")

# Valor padrão
def apresentar_lugar(lugar='nossa loja'):
    print(f"Conheça {lugar}")

apresentar_lugar()
apresentar_lugar('Disney')

# Caso existam valores padrão em uma função, esse valor padrão
# deve ser posto no final da lista de argumentos, para que
# não seja exibido uma mensagem de erro. Exemplo de cima 
# agora acrescido de horário, sendo lugar o argumento principal

def apresentar_lugar(horario_de_funcionamento, lugar='nossa loja'):
    print(f"Conheça {lugar}, horário de funcionamento {horario_de_funcionamento}")

apresentar_lugar('8:00 às 18:00', 'Disney')
# apresentar_lugar('Disney')
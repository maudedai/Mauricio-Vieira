# Vamos pensar no seguinte exemplo:
idade = 21
possui_convite = False
filho_do_dono = True
print((idade >= 21) and (possui_convite == True))
print((idade >= 21) or (possui_convite == True))
#maior de 21 e possui convite ou seja filho do dono
print((idade >21 and possui_convite == True) or (filho_do_dono == True))

#Exemplo 2

maior_de_idade = True
possui_carteira_de_trabalho = False
# você só pode trabalhar aqui se for maior de idade e possuir carteida de trabalho

print('Você pode trabalhar aqui? ', (maior_de_idade == True and possui_carteira_de_trabalho == True))

# Queremos contratar pessoas que ainda não possuem um veículo próprio, mas já possuam uma carteira de trabalho

esta_trabalhando_atualmente = True
possui_veiculo_proprio = False

print('Você se enquanda para contratação? ', 
      (possui_veiculo_proprio == False and possui_carteira_de_trabalho == True) or not possui_veiculo_proprio)
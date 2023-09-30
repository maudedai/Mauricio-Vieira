'''trabalho_terminado = False
if trabalho_terminado == True:
    print('Bora Sair!')
else:
    print('Não posso sair agora')

# até 2 atrasos posso entrar / maior do que isso devo ir para diretoria

numero_de_atrasos = 8
if numero_de_atrasos >= 3:
    print('Vá para a diretoria')
elif numero_de_atrasos ==2:
    print('Esta é a sua segunda falta')
elif numero_de_atrasos == 1:
    print('Esta é a sua primeira falta')
else:
    print('Pode entrar')'''

velocidade = 49
if velocidade <= 50:
    print('Não foi multado')
elif velocidade >= 51 and velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 1 and velocidade <=75:
    print('Levou multa e 3 pontos')
else:
    print('Levou multa e 7 pontos')

# Uso do chainging
velocidade = 77
if velocidade <= 50:
    print('Não foi multado')
elif 55 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif 61 <= velocidade <=75:
    print('Levou multa e 3 pontos')
else:
    print('Levou multa e 7 pontos')
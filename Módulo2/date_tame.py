from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
 
#como criar uma data
lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)
#quero receber a data do laçamento do meu aplicativo
#25/08/2223
data_de_lancamento = datetime.strptime(input('Quando demvemos lançar o aplictativo?'), '%d/%m/%Y')
print(type(data_de_lancamento))

#calculo entre data
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual

print(prazo.days)
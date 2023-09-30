from datetime import datetime

hoje = datetime.now()
meu_aniversario = datetime.strptime(input("Digite a data do seu próximo aniversário: "),'%d/%m/%y')
dias = meu_aniversario - hoje 
print(dias.days)
'''Desafio
Crie um decorardor que irá pegar a funçao que for passando
para ele e imprimir o horário atual antes de executar a 
função e depois  imprimir o horário após ter finalizado
a execução da função

> Dica: você terá que usar o módulo datetime para conseguir
o horário atual'''
from datetime import datetime

def meu_horario(hora):
    def horario():
        hora()
        print("Horario antes")
        hora()
        print("Depois")
    return horario

@meu_horario
def hora():
    print(datetime.now())
hora()
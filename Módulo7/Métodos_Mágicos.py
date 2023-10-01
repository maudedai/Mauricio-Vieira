# Métrodos Mágicos ( Magic Methods / dunder methods (Double underscrore))

class Pessoa:
    def __init__(self):
        self.nome = "Sou uma pessoa"
        self.habilidades = ["Habilidade 1", "Habilidade 2", "Habilidade 3"]

    #Representação para programadores(chamado métrodo repr(pessoa))
    def __repr__(self):
        return "Classe Pessoa com propriedades nome e habilidades"
    
    # O que deve ser mensurado para determnar a quandidade daquela classe(chamada com método(len(pessoa)))
    def __len__(self):
        # len(pesssoa) ??
        return len(self.habilidades)

    def __str__(self):
        return f"{self.nome} com as habilidades {self.habilidades}"


pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(pessoa)
print(dir(pessoa))
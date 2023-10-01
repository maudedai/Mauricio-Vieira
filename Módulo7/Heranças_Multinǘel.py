# Herança multinível
class Usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao
    
    def registrar_funcionario(self):
        print(f"Cadastrando usuário {self.nome}")

class Gestor(Usuario):
    def __init__(self, nome, salario, profissao, setor_responsavel):
        super().__init__(nome, salario, profissao)
        self.setor_responsavel = setor_responsavel

    def definir_setor(self, setor):
        print(f"Definindo setor para {setor}")

usuario1 = Usuario("Camilla", 500, "Analista de Software")
gestor = Gestor("Roberta", 700, "Gestora", "Gestão de Projetos")
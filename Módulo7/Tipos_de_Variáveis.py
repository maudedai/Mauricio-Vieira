class Computador:
    sistema_operacional = "Windoes 10"
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def ligar(self):
        print("Estou ligando o computador")

Computador.sistema_operacional = "Windowns"

computador1 = Computador("Asus", "8Gb", "NVidia")
computador1.marca = "Mac"
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)
Computador.sistema_operacional = "Mac"
computador2 = Computador("Dell ", "32Gb", "Radeon")
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video)
print(Computador.sistema_operacional)
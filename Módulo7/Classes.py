# Classes
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

computador1 = Computador("Asus", "8Gb", "NVidia")
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)
computador2 = Computador("Dell", "16Gb", "AMD")
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video)
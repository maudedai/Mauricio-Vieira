from abc import ABC, abstractmethod
class Monitor:
    @abstractmethod
    def aumentar_claridade(self, pontos_de_claridade):
        pass
        
    @abstractmethod
    def reduzir_claridade(self, pontos_de_claridade):
        pass


class MonitorFullHD(Monitor):
    def aumentar_claridade(self, pontos_de_claridade):
        return f"Aumentando a claridade em {pontos_de_claridade} pontos"
    def reduzir_claridade(self, pontos_de_claridade):
        return f"Diminuindo a claridade em {pontos_de_claridade} pontos"
    

monitor = MonitorFullHD()
print(monitor.aumentar_claridade(5))
print(monitor.reduzir_claridade(5))
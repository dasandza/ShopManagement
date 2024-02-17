from funcionario import *

class Vendedor(Funcionario):
    def __init__(self, nome, numero):
        super().__init__(nome, numero)
        self.faturas = []
        self.numero = str(numero)

    def obter_todas_faturas(self):
        return self.faturas

    def obter_faturas(self, inicio, fim):
        l = []
        for fatura in self.faturas:
            if int(fatura.data.ano) in range(int(inicio.ano), int(fim.ano) + 1) and int(fatura.data.mes) in range(int(inicio.mes), int(fim.mes) + 1) and int(fatura.data.dia) in range(int(inicio.dia), int(fim.dia) + 1):
                l.append(fatura)
        return l








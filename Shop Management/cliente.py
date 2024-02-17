from pessoa import *

class Cliente(Pessoa):
    def __init__(self, nome, numero):
        super().__init__(nome)
        self.numero = str(numero)
        self.faturas = []

    def obter_numero(self):
        return self.numero

    def obter_faturas(self):
        return self.faturas


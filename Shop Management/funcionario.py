from pessoa import *

class Funcionario(Pessoa):
    def __init__(self, nome, numero):
        super().__init__(nome)
        self.numero = str(numero)

    def obter_numero(self):
        return self.numero


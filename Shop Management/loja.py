from gestor import Gestor
from vendedor import Vendedor
from cliente import Cliente
from item import Item
from fatura import Fatura
from data import Data

class Loja:
    def __init__(self):
        self.gestor = None
        self.vendedores = []
        self.clientes = []
        self.itens = []

    def obter_gestor(self):
        return self.gestor

    def obter_vendedores(self):
        return self.vendedores

    def obter_clientes(self):
        return self.clientes

    def obter_itens(self):
        return self.itens

    def registar_gestor(self, nome, numero_de_funcionário):
        self.gestor = Gestor(nome, numero_de_funcionário)

    def registar_vendedor(self, nome, numero_de_funcionario):
        self.vendedores.append(Vendedor(nome, numero_de_funcionario))

    def registar_cliente(self, nome, numero_de_cliente):
        self.clientes.append(Cliente(nome, numero_de_cliente))

    def registar_fatura(self, numero_de_cliente, itens, numero_de_funcionario, ano, mes, dia):
        if len(self.clientes != 0):
            for i, c in enumerate(self.clientes):
                if c.numero == numero_de_cliente:
                    break
                elif i == len(self.clientes) - 1 and self.clientes[-1].numero != numero_de_cliente:
                    print("Cliente não encontrado.")
                    return
        else:
            print("Cliente não encontrado.")

        if len(self.vendedores != 0):
            for i, v in enumerate(self.vendedores):
                if v.numero == numero_de_funcionario:
                    break
                elif i == len(self.vendedores) - 1 and self.vendedores[-1].numero != numero_de_funcionario:
                    print("Funcionário não encontrado.")
                    return
        else:
            print("Funcionário não encontrado.")

        a = Fatura(numero_de_funcionario, Data(ano, mes, dia), c, v, itens)
        c.faturas.append(a)
        v.faturas.append(a)

    def registar_item(self, nome):
        self.itens.append(Item(nome))

    def obter_faturas_cliente(self, numero_de_cliente):
        for c in self.clientes:
            if c.numero == numero_de_cliente:
                return c.faturas

    def obter_faturas_vendedor(self, numero_de_funcionario):
        for v in self.vendedores:
            if v.numero == numero_de_funcionario:
                return v.faturas

def main():
    c = Loja()
    while True:
        try:
            cmd = int(input("\n1 - Obter Gestor\n"
                            "2 - Obter Vendedores\n"
                            "3 - Obter Clientes\n"
                            "4 - Obter Itens\n"
                            "5 - Registar Gestor\n"
                            "6 - Registar Vendedor\n"
                            "7 - Registar Cliente\n"
                            "8 - Registar Item\n"
                            "9 - Registar Fatura\n"
                            "10 - Obter Faturas de Cliente\n"
                            "11 - Obter Faturas de Vendedor\n"
                            "12 - Fechar\n"
                            ">>> "))
        except:
            continue
        else:
            if cmd == 1:
                print(f"{c.nome} - {c.numero}" if c.gestor != None else "Sem gestor registado.")
            elif cmd == 2:
                for h in c.obter_vendedores():
                    print(f"{h.nome} - {h.numero}")
            elif cmd == 3:
                for h in c.obter_clientes():
                    print(f"{h.nome} - {h.numero}")
            elif cmd == 4:
                for h in c.obter_itens():
                    print(h.nome)
            elif cmd == 5:
                nome = str(input("Nome: "))
                numero = str(input("Numero: "))
                c.registar_gestor(nome, numero)
            elif cmd == 6:
                nome = str(input("Nome: "))
                numero = str(input("Numero: "))
                c.registar_vendedor(nome, numero)
            elif cmd == 7:
                nome = str(input("Nome: "))
                numero = str(input("Numero: "))
                c.registar_cliente(nome, numero)
            elif cmd == 8:
                nome = str(input("Nome: "))
                c.registar_item(nome)
            elif cmd == 9:
                l = []
                numero_c = str(input("Numero do cliente: "))
                while True:
                    i = input("Item: ").strip()
                    if i == "":
                        break
                    else:
                        l.append(i)
                if len(l) != 0:
                    numero_f = str(input("Numero do funcionário: "))
                    ano = int(input("Ano: "))
                    mes = int(input("Mês: "))
                    dia = int(input("Dia: "))
                    c.registar_fatura(numero_c, l, numero_f, ano, mes, dia)
            elif cmd == 10:
                numero_c = str(input("Numero do cliente: "))
                print(c.obter_faturas_cliente(numero_c))
            elif cmd == 11:
                numero_f = str(input("Numero do funcionário: "))
                print(c.obter_faturas_vendedor(numero_f))
            elif cmd == 12:
                quit()
            else:
                continue

if __name__ == '__main__':
    main()

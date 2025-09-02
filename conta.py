class ContaBancaria:
    def __init__(self, titular):
            self.titular = titular
            
            self.saldo = 0

    def exibir_saldo(self):
          print("titular:", self.titular, "| Saldo: R$", self.saldo)

nome = input("Digite o nome do titular da conta: ")
conta1 = ContaBancaria(nome)
conta1.exibir_saldo()

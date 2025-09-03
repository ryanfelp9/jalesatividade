class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    
    def mostrar_saldo(self):
        return self.saldo

conta = ContaBancaria("Ryan", 1000)
conta.depositar(500)
conta.sacar(200)
print("Ryan",conta.mostrar_saldo())

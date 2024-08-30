class ContaBancaria:
    def __init__(self, numero_conta):
        self.__numero_conta = numero_conta
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor do depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")
        
minha_conta = ContaBancaria(12345)

minha_conta.depositar(1000)

minha_conta.sacar(374)

minha_conta.exibir_saldo()
import abc


class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'DEPÓSITO {valor}')

    def detalhes(self, msg=''):
        print(f'o seu saldo é {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor  # Correção aqui: self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo_saque = -self.limite

        if valor_pos_saque >= limite_maximo_saque:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado. Limite excedido.')


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.depositar(100)
    cp1.sacar(1)
    print('---')

    cc1 = ContaCorrente(111, 333, 0, 100)
    cc1.sacar(1)
    cc1.depositar(100)
    cc1.sacar(150)
    cc1.sacar(50)
    cc1.sacar(1)
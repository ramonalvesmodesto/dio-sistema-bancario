from src.model.conta import ContaCorrenteModel, ContaModel, ContaIteradorModel
from src.view.conta import ContaView

class ContaController(ContaModel):
    def __init__(self) -> None:
        super().__init__()
        self.view = ContaView()

    def nova_conta(self, cliente, numero):
        self.cliente = cliente
        self.numero = numero
        self.view.exibir_mensagem(1, self.limite)

    def sacar(self, valor):
        calculo_saldo = self.saldo - valor
        if calculo_saldo < 0:
            self.view.exibir_mensagem(2, self.limite)
            return False
        elif valor > self._limite:
            self.view.exibir_mensagem(3, self.limite)
            return False
        return True

    def depositar(self, valor):
        if self.saldo + valor <= self.saldo:
            self.view.exibir_mensagem(4, self.limite)
            return False
        return True

    def __str__(self):
        return f"Agência: {self.agencia} C/C: {self.numero}"
    
class ContaCorrenteController(ContaCorrenteModel, ContaController):
    def __init__(self) -> None:
        super().__init__()
            
    def alterar_limite_saques(self, novo_limite_saque):
        self.limite_saques = novo_limite_saque

    def alterar_limite(self, novo_limite):
        self.limite = novo_limite

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"
    
class ContaIteratorController(ContaIteradorModel):
    def __init__(self, contas):
        super().__init__(contas)
        self.view = ContaView()

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            return self.view.exibir_conta(conta)
        except IndexError:
            raise StopIteration
        finally:
            self.contador = 1

from ..model.conta import ContaModel
from ..view.conta import ContaView

class ContaController:
    def __init__(self, model: ContaModel, view: ContaView) -> None:
        self.model = model
        self.view = view

    def nova_conta(self, cliente, numero):
        self.model.cliente = cliente
        self.model.numero = numero
        self.view.exibir_mensagem(1)

    def sacar(self, valor):
        calculo_saldo = self.model.saldo - valor
        if calculo_saldo < 0:
            self.view.exibir_mensagem(2)
            return False
        elif valor > self._limite:
            self.view.exibir_mensagem(3, self.model.limite)
            return False

        return True

    def depositar(self, valor):
        if self.model.saldo + valor <= self.model.saldo:
            self.view.exibir_mensagem(4)
            return False
        return True

    def __str__(self):
        return f"Agência: {self.model.agencia} C/C: {self.model.numero}"
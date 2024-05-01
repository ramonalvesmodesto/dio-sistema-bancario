from src.model.conta import ContaModel
from src.view.conta import ContaView

class ContaController(ContaModel):
    def __init__(self) -> None:
        super().__init__()
        self.view = ContaView

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
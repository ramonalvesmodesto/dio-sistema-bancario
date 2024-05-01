from src.model.conta import ContaModel
from src.model.transacao import DepositoModel, SaqueModel
from src.view.transacao import DepositoView, SaqueView

class DespositoController(DepositoModel):
    def __init__(self, valor=0.0):
        super().__init__(valor)
        self.view = DepositoView()

    def registrar(self, conta: ContaModel):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(DespositoController(self.valor))
            conta.saldo = self.valor
            self.view.exibir_mensagem()

    def __str__(self):
        return f"Depósito: +{self.valor:.2f} - {self.data_hora_transacao}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.data_hora_transacao}')>"

class SaqueController(SaqueModel):
    def __init__(self, valor=0.0):
        super().__init__(valor)
        self.view = SaqueView()

    def registrar(self, conta: ContaModel):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(SaqueController(self.valor))
            conta.saldo =- self.valor
            self.view.exibir_mensagem()

    def __str__(self):
        return f"Saque: -{self.valor:.2f} - {self.data_hora_transacao}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.data_hora_transacao}')>"

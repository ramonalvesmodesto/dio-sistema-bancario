from src.controller.historico import HistoricoController


class ContaModel:
    def __init__(self):
        self._saldo = 0
        self._numero = ""
        self._agencia = "0001"
        self._cliente = ""
        self._historico = HistoricoController()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo += valor

    @saldo.deleter
    def saldo(self, valor):
        self._saldo -= valor

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def historico(self):
        return self._historico
    
class ContaCorrenteModel(ContaModel):
    def __init__(self, limite=500.0, limite_saques=10):
        super().__init__()
        self._limite: float = limite
        self._limite_saques:float = limite_saques

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def limite_saques(self):
        return self._limite_saques
    
    @limite_saques.setter
    def limite_saques(self, limite_saques):
        self._limite_saques = limite_saques

class ContaIteradorModel:
    def __init__(self, contas):
        self._contas = contas
        self._contador = 0

    @property
    def contas(self):
        return self._contas
    
    @property
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self, numero):
        self._contador += numero

    def __iter__(self):
        return self

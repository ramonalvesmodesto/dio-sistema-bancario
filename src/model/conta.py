class ContaModel:
    def __init__(self):
        self._saldo = 0
        self._numero = ""
        self._agencia = "0001"
        self._cliente = ""
        self._historico = Historico()

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
    def cliente(self, numero):
        self._cliente = numero

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
class HistoricoModel:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

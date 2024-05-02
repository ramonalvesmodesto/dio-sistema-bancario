from abc import ABC, abstractmethod
from datetime import datetime

from src.model.conta import ContaModel


class TransacaoModel(ABC):
    @abstractmethod
    def registrar(conta: ContaModel):
        pass

class DepositoModel(TransacaoModel):
    def __init__(self, valor=0.0):
        self._valor = valor
        self._data_hora_transacao: datetime = datetime.now()

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def data_hora_transacao(self):
        return self._data_hora_transacao
    
    @data_hora_transacao.setter
    def data_hora_transacao(self, data_hora_transacao):
        self._data_hora_transacao = data_hora_transacao

class SaqueModel(TransacaoModel):
    def __init__(self, valor=0.0):
        self._valor = valor
        self._data_hora_transacao: datetime = datetime.now()

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def data_hora_transacao(self):
        return self._data_hora_transacao
    
    @data_hora_transacao.setter
    def data_hora_transacao(self, data_hora_transacao):
        self._data_hora_transacao = data_hora_transacao


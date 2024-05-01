from src.model.endereco import EnderecoModel


class ClienteModel:
    def __init__(self, endereco: EnderecoModel = ""):
        self._endereco = endereco
        self._contas = []
        self._conta_principal = ""

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @endereco.deleter
    def endereco(self):
        self._endereco = ""

    @property
    def contas(self):
        return self._contas
    
    @contas.setter
    def contas(self, contas):
        self._contas = contas

    @property
    def conta_principal(self):
        return self._conta_principal

    @conta_principal.setter
    def conta_principal(self, conta):
        self._conta_principal = conta

    @conta_principal.deleter
    def conta_principal(self):
        self._conta_principal = ""

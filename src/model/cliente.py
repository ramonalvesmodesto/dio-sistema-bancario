from src.model.pessoaFisica import PessoaFisicaModel
from src.model.endereco import EnderecoModel


class ClienteModel(PessoaFisicaModel):
    def __init__(self, cpf, nome, data_nascimento, endereco: EnderecoModel = ""):
        super().__init__(cpf, nome, data_nascimento)
        self._endereco = endereco
        self._conta = ""

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
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta

from src.model.endereco import EnderecoModel


class PessoaFisicaModel:
    def __init__(self, cpf, nome, data_nascimento, endereco: EnderecoModel = ""):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    def __str__(self):
        return f"{', '.join([f'{conta}' for conta in self._contas])}\n"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.cpf}')>"

class EnderecoModel:
    def __init__(self, logradouro, numero, estado, cidade, bairro):
        self._logradouro = logradouro
        self._numero = numero
        self._estado = estado
        self._cidade = cidade
        self._bairro = bairro

    @property
    def logradouro(self):
        return self._logradouro

    @property
    def numero(self):
        return self._numero

    @property
    def estado(self):
        return self._estado

    @property
    def cidade(self):
        return self._cidade

    @property
    def bairro(self):
        return self._bairro

    def __str__(self):
        return f"Logradouro: {self._logradouro} \nNúmero: {self._numero} \nEstado: {self._estado} \
            \nCidade: {self._cidade} \nBairro: {self._bairro}"

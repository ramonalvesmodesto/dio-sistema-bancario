from src.model.cliente import ClienteModel
from src.model.conta import ContaModel


class BancoModel:
    def __init__(self):
        self._ultimo_valor_deposito:float = 0
        self._clientes: list[ClienteModel] = []
        self._id_cliente_logado: str = None
        self._cliente_logado = ''
        self._numero_conta_corrente: int = 1
        self._conta_corrente_cliente_sessao_logada: ContaModel = ""

    @property
    def ultimo_valor_deposito(self):
        return self._ultimo_valor_deposito

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, cliente: ClienteModel):
        self._clientes.append(cliente)

    @property
    def id_cliente_logado(self):
        return self._id_cliente_logado

    @id_cliente_logado.setter
    def id_cliente_logado(self, id):
        self._id_cliente_logado = id

    @property
    def cliente_logado(self):
        return self._cliente_logado

    @cliente_logado.setter
    def cliente_logado(self, cliente: ClienteModel):
        if cliente is not None:
            self._cliente_logado = cliente
            self._id_cliente_logado = cliente.cpf
            
    @property
    def numero_conta_corrente(self):
        return self._numero_conta_corrente

    @numero_conta_corrente.setter
    def numero_conta_corrente(self, numero):
        self._numero_conta_corrente += numero

    @property
    def conta_corrente_cliente_sessao_logada(self):
        return self._conta_corrente_cliente_sessao_logada

    @conta_corrente_cliente_sessao_logada.setter
    def conta_corrente_cliente_sessao_logada(self, conta_corrente):
        self._conta_corrente_cliente_sessao_logada = conta_corrente

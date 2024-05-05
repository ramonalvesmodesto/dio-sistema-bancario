from src.model.banco import BancoModel
from src.controller.log import log_banco
from src.controller.conta import ContaIteratorController


class BancoView:
    @log_banco
    def exibir_contas(self, clientes):
        for cliente in clientes:
            cliente.listar_conta()

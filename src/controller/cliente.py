from src.controller.log import log_banco
from src.controller.conta import ContaIteratorController
from src.model.endereco import EnderecoModel
from src.model.conta import ContaModel
from src.model.transacao import TransacaoModel
from src.model.cliente import ClienteModel
from src.view.cliente import ClienteView


class ClienteController(ClienteModel):
    def __init__(self, cpf, nome, data_nascimento, endereco: EnderecoModel = ""):
        super().__init__(cpf, nome, data_nascimento, endereco)
        self.view = ClienteView()

    def realizar_transacao(self, conta: ContaModel, transacao: TransacaoModel):
        tipo_transacao = transacao.__class__.__name__
        transacoes_do_dia = conta.historico.transacoes_do_dia(tipo_transacao)

        if len(transacoes_do_dia) < conta.limite_saques:
            transacao.registrar(conta)
        else:
            self.view.exibir_mensagem(conta.limite_saques, tipo_transacao)

    @log_banco
    def cadastro_endereco(self, logradouro, numero, estado, cidade, bairro):
        endereco = EnderecoModel(logradouro, numero, estado, cidade, bairro)
        self.endereco = endereco

    @log_banco
    def listar_conta(self):
        self.conta.view.exibir_conta(self.conta)

    def adicionar_conta(self, conta: ContaModel):
        self.conta = conta

    def __str__(self) -> str:
        return f"{self._endereco}, {self._conta_principal}, {self._contas}"

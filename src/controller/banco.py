from src.controller.cliente import ClienteController
from src.controller.conta import ContaCorrenteController
from src.controller.log import log_banco
from src.model.endereco import EnderecoModel
from src.model.pessoaFisica import PessoaFisicaModel
from src.model.transacao import TransacaoModel
from src.model.banco import BancoModel
from src.view.banco import BancoView



class BancoController(BancoModel):
    def __init__(self):
        super().__init__()
        self.view = BancoView()

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf: return cliente
        return None
    
    @log_banco
    def login(self, cpf):
        cliente = self.buscar_cliente(cpf)

        if cliente is None: print("\nUsuário não encontrado\n")

        return cliente

    @log_banco
    def criar_conta(self, cliente: ClienteController):
        nova_conta_corrente = ContaCorrenteController()
        nova_conta_corrente.nova_conta(cliente, self.numero_conta_corrente)
        self.numero_conta_corrente = 1
        cliente.adicionar_conta(nova_conta_corrente)

    @log_banco
    def transacao(self, transacao: TransacaoModel, valor):
        nova_transacao = transacao(valor)
        self.cliente_logado.realizar_transacao(
            self.cliente_logado.conta, nova_transacao
        )

    @log_banco
    def cadastro_cliente(self, cpf, nome, data_nascimento, endereco):
        endereco = EnderecoModel(endereco['logradouro'], endereco['numero'], endereco['estado'], endereco['cidade'], endereco['bairro'])
        cliente = ClienteController(cpf, nome, data_nascimento, endereco)
        self.clientes = cliente    
        return cliente    

    @log_banco
    def listar_clientes(self):
        self.view.exibir_contas(self.clientes)

    @log_banco
    def listar_extrato(self, historico, tipo):
        self.cliente_logado.conta.historico.listar_historico_transacoes(historico, tipo)

    def __str__(self):
        return f"{self._cliente_logado}, {self.ultimo_valor_deposito}, {self._clientes}, {self._id_cliente_logado}, \
            {self._numero_conta_corrente}, {self._conta_corrente_cliente_sessao_logada}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.numero_conta_corrente}', \
                '{self.conta_corrente_cliente_sessao_logada}')>"

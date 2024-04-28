import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class ContaIterador:
    def __init__(self, contas):
        self._contas = contas
        self._contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self._contas[self._contador]
            return textwrap.dedent(
                f"""
                Nome: {conta.cliente.nome}
                C/C: {conta.numero}
                Agência: {conta.agencia}
                Saldo: {conta.saldo}
            """
            )
        except IndexError:
            raise StopIteration
        finally:
            self._contador += 1


class Conta:
    def __init__(self):
        self._saldo = 0
        self._numero = ""
        self._agencia = "0001"
        self._cliente = ""
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo += valor

    @saldo.deleter
    def saldo(self, valor):
        self._saldo -= valor

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def nova_conta(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero
        print("\nConta criada com sucesso!!\n")

    def sacar(self, valor):
        calculo_saldo = self._saldo - valor
        if calculo_saldo < 0:
            print(
                "\nNão foi possível autorizar o saque! O valor de saque excedeu seu saldo!\n"
            )
            return False
        elif valor > self._limite:
            print(
                f"\nNão foi possível realizar o saque! Seu limite de saque é: R${self._limite: .2f}"
            )
            return False

        return True

    def depositar(self, valor):
        if self._saldo + valor <= self._saldo:
            print(
                "\nNão é permitido depósitos de valores iguais ou menores que zero!\n"
            )
            return False

        return True

    def __str__(self):
        return f"Agência: {self._agencia} C/C: {self._numero}"


class ContaCorrente(Conta):
    def __init__(self, limite=500.0, limite_saques=10):
        super().__init__()
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def alterar_limite_saques(self, novo_limite_saque):
        self._limite_saques = novo_limite_saque

    def alterar_limite(self, novo_limite):
        self._limite = novo_limite

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"


class Transacao(ABC):
    @abstractmethod
    def registrar(conta: Conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor=0.0):
        self._valor = valor
        self._data_hora_transacao = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def data_hora_transacao(self):
        return self._data_hora_transacao

    def registrar(self, conta: Conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(Deposito(self._valor))
            conta.saldo = self.valor
            print("\nDepósito realizado com sucesso!!\n")

    def __str__(self):
        return f"Depósito: +{self._valor:.2f} - {self._data_hora_transacao}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.data_hora_transacao}')>"


class Saque(Transacao):
    def __init__(self, valor=0.0):
        self._valor = valor
        self._data_hora_transacao = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def data_hora_transacao(self):
        return self._data_hora_transacao

    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(Saque(self._valor))
            conta.saldo = -self._valor
            print("\nSaque realizado com sucesso!!\n")

    def __str__(self):
        return f"Saque: -{self._valor:.2f} - {self._data_hora_transacao}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.data_hora_transacao}')>"


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao == str(transacao.__class__.__name__):
                yield transacao
            elif tipo_transacao == str(transacao.__class__.__name__):
                yield transacao
            elif tipo_transacao is None:
                yield transacao

    def transacoes_do_dia(self, tipo_transacao):
        data_atual = datetime.now().date()
        transacoes = []

        for transacao in self._transacoes:
            if (
                datetime.strptime(
                    transacao.data_hora_transacao, "%d-%m-%Y, %H:%M:%S"
                ).date()
                == data_atual
                and transacao.__class__.__name__ == tipo_transacao
            ):
                transacoes.append(transacao)
        return transacoes

    def __str__(self) -> str:
        return f"\nExtrato: \n{', '.join([f'{transacao}' for transacao in self.transacoes])}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self._transacoes}')>"


class Endereco:
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


class Cliente:
    def __init__(self, endereco: Endereco = ""):
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

    @property
    def conta_principal(self):
        return self._conta_principal

    @conta_principal.setter
    def conta_principal(self, conta):
        self._conta_principal = conta

    @conta_principal.deleter
    def conta_principal(self):
        self._conta_principal = ""

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        tipo_transacao = transacao.__class__.__name__
        transacoes_do_dia = conta.historico.transacoes_do_dia(tipo_transacao)

        if len(transacoes_do_dia) < conta.limite_saques:
            transacao.registrar(conta)
        else:
            print(f"\nVocê excedeu o limite de {conta.limite_saques} {tipo_transacao}s")

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)

    def __str__(self) -> str:
        return f"{self._endereco}, {self._conta_principal}, {self._contas}"


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco: Endereco = ""):
        super().__init__(endereco)
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


class Banco:
    def __init__(self):
        self._ultimo_valor_deposito = 0
        self._clientes = []
        self._id_cliente_logado = None
        self._cliente_logado = Cliente()
        self._numero_conta_corrente = 1
        self._conta_corrente_cliente_sessao_logada: Conta = ""

    @property
    def ultimo_valor_deposito(self):
        return self._ultimo_valor_deposito

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, cliente: Cliente):
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
    def cliente_logado(self, cliente: Cliente):
        if cliente is not None:
            self._cliente_logado = cliente
            self._id_cliente_logado = cliente.cpf
            self._conta_corrente_cliente_sessao_logada = cliente.conta_principal

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

    def buscar_cliente(self, cpf):
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente

        return None

    def __str__(self):
        return f"{self._cliente_logado}, {self.ultimo_valor_deposito}, {self._clientes}, {self._id_cliente_logado}, \
            {self._numero_conta_corrente}, {self._conta_corrente_cliente_sessao_logada}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.numero_conta_corrente}', \
                '{self.conta_corrente_cliente_sessao_logada}')>"

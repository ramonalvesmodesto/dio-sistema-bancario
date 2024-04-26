from datetime import datetime 
import textwrap
from abc import ABC, abstractmethod

class Conta:
    def __init__(self):
        self._saldo = 0
        self._numero = ''
        self._agencia = '0001'
        self._cliente = ''
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
        print('\nConta criada com sucesso!!\n')

    def sacar(self, valor):
        calculo_saldo = self._saldo - valor
        if calculo_saldo <= 0:
            print('\nNão foi possível autorizar o saque! O valor de saque excedeu seu saldo!\n')
            return False
        
        return True

    def depositar(self, valor):
        if self._saldo + valor <= self._saldo:
            print('\nNão é permitido depósitos de valores iguais ou menores que zero!\n')
            return False
        
        return True
    
    def __str__(self):
        return f"Agência: {self._agencia} C/C: {self._numero}"
    
class ContaCorrente(Conta):
    def __init__(self, limite = 500.0, limite_saques = 3):
        super().__init__()
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self.limite_saques
    
    @limite.setter
    def limite_saques(self, valor):
        self._limite_saques -= valor
    
    def sacar(self, valor):
        calculo_saldo = self._saldo - valor

        if calculo_saldo <= 0:
            print('\nNão foi possível autorizar o saque! O valor de saque excedeu seu saldo!\n')
            return False
        elif self._limite_saques == 0:
            print(f'\nSeu limite de saque diário foi excedido! Seu limite de saque é {self._limite_saques}, e você esgotou seus saques diários')
            return False
        elif valor > self._limite:
            print(f'\nNão foi possível realizar o saque! Seu limite de saque é: R${self._limite: .2f}')
            return False
        
        return True
    
    def alterar_limite_saques(self, novo_limite_saque):
        self._limite_saques = novo_limite_saque

    def alterar_limite(self, novo_limite):
        self._limite = novo_limite
    
class Transacao(ABC):
    @abstractmethod
    def registrar(conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor=0):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    
    def registrar(self, conta: Conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(Deposito(self._valor))
            conta.saldo = self.valor
            print('\nDepósito realizado com sucesso!!\n')

    def __str__(self):
        return f"Depósito: +{self._valor:.2f} - {datetime.now()}"

class Saque(Transacao):
    def __init__(self, valor=0):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    
    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(Saque(self._valor))
            conta.saldo = -self._valor
            conta.limite_saques = 1
            print('\nSaque realizado com sucesso!!\n')

    def __str__(self):
        return f"Saque: -{self._valor:.2f} - {datetime.now()}"
    
class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)

    def __str__(self) -> str:
        return f"\nExtrato: \n{', '.join([f'{transacao}' for transacao in self._transacoes])}"

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
        return f"Logradouro: {self._logradouro} \nNúmero: {self._numero} \nEstado: {self._estado} \nCidade: {self._cidade} \nBairro: {self._bairro}"

class Cliente:
    def __init__(self, endereco: Endereco = ''):
        self._endereco = endereco
        self._contas = []
        self._conta_principal = ''

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @endereco.deleter
    def endereco(self):
        self._endereco = ''

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
        self._conta_principal = ''
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)

    def __str__(self) -> str:
        return f"{self._endereco}, {self._conta_principal}, {self._contas}"

class PessoaFisica(Cliente):
    def __init__(self, endereco: Endereco, cpf, nome, data_nascimento):
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
    
class Banco:
    def __init__(self):
        self._ultimo_valor_deposito = 0
        self._clientes = []
        self._id_cliente_logado = None
        self._cliente_logado = Cliente()
        self._numero_conta_corrente = 1
        self._conta_corrente_cliente_sessao_logada = ''

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
        if cliente != None:
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
    def conta_corrente_cliente_sessao_logada (self):
        return self._conta_corrente_cliente_sessao_logada
    
    @conta_corrente_cliente_sessao_logada.setter
    def conta_corrente_cliente_sessao_logada (self, conta_corrente):
        self._conta_corrente_cliente_sessao_logada = conta_corrente

    def buscar_cliente(self, cpf):
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
        
        return None
    
    def __str__(self):
        return f"{self._cliente_logado}, {self.ultimo_valor_deposito}, {self._clientes}, {self._id_cliente_logado}, {self._numero_conta_corrente}, {self._conta_corrente_cliente_sessao_logada}"

def menu_login_cadastro ():
    menu = '''
    =============== Menu ===============         
    [1] - Fazer login
    [2] - Realizar cadastro
    [q] - Sair 
    ======================================
    '''
    return textwrap.dedent(menu)

def menu_movimentacao_conta (saldo, deposito, usuario):
    menu = f'''\n
    =============== Menu ===============
    Saldo: R${saldo: .2f}     
    Último Depósito: R${deposito: .2f}
    Usuário: {usuario}

    [1] - \tDepósito       
    [2] - \tSaque          
    [3] - \tExtrato
    [4] - \tCriar Conta   
    [5] - \tExibir Contas     
    [q] - \tSair
    ======================================         
    '''
    return textwrap.dedent(menu)

def login(banco: Banco):
    cpf = input('Insira seu CPF: ')
    cliente = banco.buscar_cliente(cpf)
    
    if cliente == None:
        print('\nUsuário não encontrado\n')   
    
    return cliente

def criar_conta(banco: Banco):
    nova_conta_corrente = ContaCorrente()
    nova_conta_corrente.nova_conta(banco.cliente_logado, banco.numero_conta_corrente)
    banco.numero_conta_corrente = 1
    banco.cliente_logado.adicionar_conta(nova_conta_corrente)
    if len(banco.cliente_logado.contas) == 0: banco.cliente_logado.conta_principal = nova_conta_corrente

def transacao(banco: Banco, transacao: Transacao):
    valor = float(input(f'Digite o valor para {transacao.__class__.__name__}: '))
    transacao.valor = valor
    banco.cliente_logado.realizar_transacao(banco.conta_corrente_cliente_sessao_logada, transacao)

def cadastro():
    nome = input('Informe seu nome: ')
    cpf = input('Informe seu CPF: ')
    data_nascimento = input('Informe sua data de nascimento: ')

    logradouro = input('Informe seu logradouro: ')
    numero = input('Informe o número de sua casa: ')
    bairro = input('Informe seu bairro: ')
    cidade = input('Informe sua cidade: ')
    estado = input('Informe seu estado (XX): ')

    endereco = Endereco(logradouro, numero, estado, cidade, bairro)
    cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
    return cliente

def main ():
    banco = Banco()

    while True:
        if banco.id_cliente_logado == None:
            print(menu_login_cadastro())
            opcao = str(input('Escolha uma opção: '))

            if opcao == '1':
                banco.cliente_logado = login(banco)
            elif opcao == '2':
                cliente = cadastro()
                banco.clientes = cliente
            elif opcao == 'q':
                break

            continue

        if len(banco.cliente_logado.contas) == 0:
            opcao = str(input('\nVocê não possui uma conta corrente, deseja criar uma? 1 para sim, 2 para não \n=> '))
            if opcao == '1':
               criar_conta(banco)
            else:
                continue

        print(menu_movimentacao_conta(banco.conta_corrente_cliente_sessao_logada.saldo, banco.ultimo_valor_deposito, banco.id_cliente_logado))
        entrada = str(input('Digite sua escolha: '))
        
        if entrada == '1':
            transacao(banco, Deposito())      
        if entrada == '2':
            transacao(banco, Saque())        
        if entrada == '3':
            print(banco.conta_corrente_cliente_sessao_logada.historico)
        if entrada == '4':
            criar_conta(banco)
        if entrada == '5':
            print(banco.cliente_logado)
        if entrada == 'q':
            banco.id_cliente_logado = None


main()
                
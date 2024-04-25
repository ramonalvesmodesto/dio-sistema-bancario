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
        if self._limite_saques == 0:
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
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(Deposito(self._valor))
            conta.saldo = self.valor
            print('\nDepósito realizado com sucesso!!\n')

    def __str__(self):
        return f"Depósito: +{self._valor:.2f}"

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(Saque(self._valor))
            conta.saldo = -self._valor
            conta.limite_saques = 1
            print('\nSaque realizado com sucesso!!\n')

    def __str__(self):
        return f"Saque: -{self._valor:.2f}"
    
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
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)


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

def menu_login_cadastro ():
    menu = '''
    =============== Menu ===============
            
    [1] - Fazer login
    [2] - Realizar cadastro
      
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

def existe_cadastro (cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
        
    return False

def login(usuarios):
    cpf = input('Insira seu CPF: ')
    if existe_cadastro(cpf, usuarios):
        return cpf
    else:
        print('\nUsuário não encontrado\n')

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
    valor_deposito = 0
    usuarios = []
    id_cliente_logado = ''
    cliente = Cliente()
    numero_conta_corrente = 1
    conta_corrente = ContaCorrente()

    login(usuarios)

    while True:
        if id_cliente_logado == '':
            cliente = cadastro()
            id_cliente_logado = cliente.cpf
            continue

        if len(cliente.contas) == 0:
            opcao = str(input('\nVocê não possui uma conta corrente, deseja criar uma? 1 para sim, 2 para não \n=> '))
            if opcao == '1':
                conta_corrente = ContaCorrente()
                conta_corrente.nova_conta(cliente, numero_conta_corrente)
                cliente.adicionar_conta(conta_corrente)
            else:
                continue

        print(menu_movimentacao_conta(conta_corrente.saldo, valor_deposito, id_cliente_logado))
        entrada = str(input('Digite sua escolha: '))
        
        if entrada == '1':
            valor_deposito = float(input('Digite o valor para depósito: '))
            deposito = Deposito(valor_deposito)
            cliente.realizar_transacao(conta_corrente, deposito)
            
        
        if entrada == '2':
            valor_saque = float(input('Digite o valor de saque: '))
            saque = Saque(valor_saque)
            cliente.realizar_transacao(conta_corrente, saque)
        
        if entrada == '3':
            print(conta_corrente.historico)

        if entrada == '4':
            numero_conta_corrente += 1
            nova_conta_corrente = ContaCorrente()
            nova_conta_corrente.nova_conta(cliente, numero_conta_corrente)
            cliente.adicionar_conta(nova_conta_corrente)

        if entrada == '5':
            print(cliente)
                    
        if entrada == 'q':
            break


main()
                
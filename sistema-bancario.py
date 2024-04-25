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
        return f"Agência: {self._agencia} \nC/C: {self._numero}\n"
    
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
            conta.saldo(self.valor)
            print('\nDepósito realizado com sucesso!!\n')

    def __str__(self):
        return f"Depósito: +{self._valor}"

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(Saque(self._valor))
            conta.saldo(-self._valor)
            print('\nSaque realizado com sucesso!!\n')

    def __str__(self):
        return f"Saque: -{self._valor}"
    
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
    def __init__(self, endereco: Endereco):
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
        pass

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
        return f"CPF: {self._cpf} \nNome: {self._nome} \nData de nascimento: {self._data_nascimento} "


def saque (saldo, valor, extrato, limite, numero_saques, limite_saques,/):
    calculo_saldo = saldo - valor
    novo_saldo = saldo
    extrato_saque = extrato.copy()

    if saldo == 0:
        print('\nVocê não possui saldo!')
    elif numero_saques == 0:
        print(f'\nSeu limite de saque diário foi excedido! Seu limite de saque é {limite_saques}, e você esgotou seus saques diários')
    elif calculo_saldo < 0:            
        print('\nNão foi possível autorizar o saque! O valor de saque excedeu seu saldo!')
    elif valor > limite:
            print(f'\nNão foi possível realizar o saque! Seu limite de saque é: R${limite: .2f}')
    else:
        novo_saldo = saldo - valor
        extrato_saque.append(valor)
        
    return novo_saldo, extrato_saque

def deposito (*, saldo, valor, extrato):
    novo_saldo = saldo
    extrato_deposito = extrato.copy()

    novo_saldo = saldo + valor
    extrato_deposito.append(valor)

    return novo_saldo, extrato_deposito

def exibir_extrato (deposito, /, *, saque): 
    print('\n=================== Extrato ===================')

    if len(deposito) == 0:
        print('\nNão foram realizadas movimentações de depósito!\n')
    else:
        print('\nDepósitos: ')
        exibir_depositos(deposito)
    
    if len(saque) == 0:
        print('\nNão foram realizadas movimentações de saque!\n')
    else:
        print('\nSaques: ')
        exibir_saques(saque)

    print('===============================================')

def exibir_depositos (deposito):
    for valor in deposito:
        print(f'R${valor: .2f}')

def exibir_saques (saque):
    for valor in saque:
        print(f'R$ -{valor: .2f}')

def login ():
    cpf = input('Digite o seu CPF: ')
    return cpf


def criar_usuario (cpf, nome, data_nascimento, endereco):
    return {
        'id': cpf,
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereco': endereco,
    }

def gerar_conta_corrente (cpf, agencia, numero_conta, contas):
    contas.append({
        'agencia': agencia,
        'numero_conta': numero_conta,
        'cpf': cpf
    })

def criar_conta(usuarios, contas, agencia, conta_corrente): 
    cpf = cadastro(usuarios)
    gerar_conta_corrente(cpf,agencia, conta_corrente, contas)

    return cpf


def existe_cadastro (cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
        
    return False

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

def listar_contas_corrente (contas):
    if len(contas) == None:
        print('\nNenhuma conta foi encontrada')
    for conta in contas:
        agencia = conta['agencia']
        numero_conta = conta['numero_conta']

        print('\n===========================\n')
        print(f'Agência: {agencia}')
        print(f'C/C :{numero_conta}')
        print('\n===========================')

def login_cadastro (usuarios, contas, agencia, conta_corrente):
    print(menu_login_cadastro())
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cpf = input('Insira seu CPF: ')
        if existe_cadastro(cpf, usuarios):
            return cpf
        else:
            print('\nUsuário não encontrado\n')
    elif opcao == '2':
        usuario = criar_conta(usuarios, contas, agencia, conta_corrente)

        return usuario
    
    return ''

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
    saldo_conta = 0
    valor_deposito = 0
    limite_saque_diario = 3
    numero_saques = limite_saque_diario
    extrato_deposito = []
    extrato_saque = []
    usuarios = []
    contas = []
    cliente_logado = ''
    agencia = '0001'
    conta_corrente = 1

    LIMITE_SAQUE = 500

    login(usuarios)

    while True:
        if cliente_logado == '':
            cadastro_cliente = cadastro()
            cliente_logado = cadastro_cliente.cpf
            continue

        print(menu_movimentacao_conta(saldo_conta, valor_deposito, cliente_logado))
        
        entrada = str(input('Digite sua escolha: '))
        
        if entrada == '1':
            valor_deposito = float(input('Digite o valor para depósito: '))

            if valor_deposito < 0:
                print('Não é permitido depósitos de valores iguais ou menores que zero!')
                continue

            resultado = deposito(saldo=saldo_conta, valor=valor_deposito, extrato=extrato_deposito)
            saldo_conta = resultado[0]
            extrato_deposito = resultado[1].copy()
            
        
        if entrada == '2':
            valor_saque = int(input('Digite o valor de saque: '))
            resultado = saque(saldo_conta, valor_saque, extrato_saque, LIMITE_SAQUE, numero_saques, limite_saque_diario)
            if resultado[0] < saldo_conta:
                numero_saques -= 1
                saldo_conta = resultado[0]
                extrato_saque = resultado[1].copy()
        
        if entrada == '3':
            exibir_extrato(extrato_deposito, saque = extrato_saque)

        if entrada == '4':
            conta_corrente += 1
            gerar_conta_corrente(cliente_logado, agencia, conta_corrente, contas)

        if entrada == '5':
            listar_contas_corrente(contas)
                    
        if entrada == 'q':
            break


main()
                
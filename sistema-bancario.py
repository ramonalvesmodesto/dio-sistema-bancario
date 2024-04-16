import textwrap

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

def criar_endereco ():
    logradouro = input('Informe seu logradouro (Rua/Nº): '),
    bairro = input('Informe seu bairro: ')
    cidade = input('Informe sua cidade: ')
    estado = input('Informe seu estado (XX): ')

    return f'{logradouro} - {bairro} - {cidade}/{estado}'

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

def cadastro (usuarios):
    nome = input('Informe seu nome: ')
    cpf = input('Informe seu CPF: ')
    data_nascimento = input('Informe sua data de nascimento: ')
    endereco = criar_endereco()
    usuario = {
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    }

    usuarios.append(usuario)

    return cpf

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

def main ():
    saldo_conta = 0
    valor_deposito = 0
    limite_saque_diario = 3
    numero_saques = limite_saque_diario
    extrato_deposito = []
    extrato_saque = []
    usuarios = []
    contas = []
    usuario_logado = ''
    agencia = '0001'
    conta_corrente = 1

    LIMITE_SAQUE = 500

    while True:
        if usuario_logado == '':
            usuario_logado = login_cadastro(usuarios, contas, agencia, conta_corrente)
            continue

        print(menu_movimentacao_conta(saldo_conta, valor_deposito, usuario_logado))
        
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
            gerar_conta_corrente(usuario_logado, agencia, conta_corrente, contas)

        if entrada == '5':
            listar_contas_corrente(contas)
                    
        if entrada == 'q':
            break


main()
                
saldo_conta = 0
valor_deposito = 0
limite_saque_diario = 3
numero_saques = limite_saque_diario
extrato_deposito = []
extrato_saque = []
usuarios = []
contas = []
usuario_logado = ''

LIMITE_SAQUE = 500

def saque (saldo, valor, extrato, limite, numero_saques, limite_saques,/):
    calculo_saldo = saldo - valor
    novo_saldo = saldo
    extrato_saque = extrato.copy()

    if saldo == 0:
        print('Você não possui saldo!')
    elif numero_saques == 0:
        print(f'Seu limite de saque diário foi excedido! Seu limite de saque é {limite_saques}, e você esgotou seus saques diários')
    elif calculo_saldo < 0:            
        print('Não foi possível autorizar o saque! O valor de saque excedeu seu saldo!')
    elif valor > limite:
            print(f'Não foi possível realizar o saque! Seu limite de saque é: R${limite: .2f}')
    else:
        novo_saldo = saldo - valor
        extrato_saque.append(valor)
        
    return novo_saldo, extrato_saque

def deposito (*, saldo, valor, extrato):
    novo_saldo = saldo
    extrato_deposito = extrato.copy()

    novo_saldo = saldo + valor
    extrato_deposito.append(valor_deposito)

    return novo_saldo, extrato_deposito

def exibir_extrato (deposito, saque): 
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
    logradouro = input('Informe seu logradouro: '),
    bairro = input('Informe seu bairro: ')
    cidade = input('Informe sua cidade: ')
    estado = input('Informe seu estado no formato XX: ')

    return f'{logradouro} - {bairro} - {cidade}/{estado}'

def criar_usuario (cpf, nome, data_nascimento, endereco):
    return {
        'id': cpf,
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereco': endereco,
    }

def gerar_conta_corrente (cpf):
    return {
        'agencia': '0234',
        'numero_conta': '1234555454',
        'cpf': cpf
    }

def cadastro ():
    nome = input('Informe seu nome: ')
    cpf = input('Informe seu CPF: ')
    data_nascimento = input('Informe sua data de nascimento: ')
    endereco = criar_endereco()

    return {
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    }

def criar_conta(): 
    dados_usuario = cadastro()
    conta_corrente = gerar_conta_corrente(dados_usuario['cpf'])

    return dados_usuario, conta_corrente

def existe_cadastro (cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
        
    return False

def exibir_opcoes_login_cadastro ():
    print('''              
        [1] - Fazer login
        [2] - Realizar cadastro
    ''')

def exibir_opcoes_movimentacao_conta (saldo, deposito, usuario):
    print(f'''
        \n\nEscolha uma opção: 
        
        Saldo: R${saldo: .2f}     
        Último Depósito: R${deposito: .2f}
        Usuário: {usuario}

        [1] - Depósito       
        [2] - Saque          
        [3] - Extrato        
        [q] - Sair            
    ''')

def login_cadastro (usuarios, contas):
    lista_usuarios = usuarios.copy()
    lista_contas = contas.copy()

    exibir_opcoes_login_cadastro()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cpf = input('Insira seu CPF: ')
        if existe_cadastro(cpf, usuarios):
            return cpf, lista_usuarios, lista_contas
        else:
            print('\nUsuário não encontrado\n')
    elif opcao == '2':
        resultado = criar_conta()

        lista_usuarios.append(resultado[0])
        lista_contas.append(resultado[1])

        return resultado[0]['cpf'], lista_usuarios, lista_contas
    
    return '', usuarios, lista_contas

while True:
    if usuario_logado == '':
        resultado = login_cadastro(usuarios, contas)
        usuario_logado = resultado[0]
        usuarios = resultado[1]
        contas = resultado[2]
        continue

    exibir_opcoes_movimentacao_conta(saldo_conta, valor_deposito, usuario_logado)
    
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
        exibir_extrato(extrato_deposito, extrato_saque)
                
    if entrada == 'q':
        break



            
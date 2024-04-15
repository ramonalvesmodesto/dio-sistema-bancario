saldo_conta = 0
valor_deposito = 0
limite_saque_diario = 3
numero_saques = limite_saque_diario
extrato_deposito = []
extrato_saque = []

LIMITE_SAQUE = 500

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques,/):
    calculo_saldo = saldo - valor
    novo_saldo = saldo
    extrato_saque = extrato.copy()

    if saldo == 0:
        print('Você não possui saldo!')
    elif numero_saques == 0:
        print(f'Seu limite de saque diário foi excedido! Seu limite de saque é {limite_saques}, e você realizou esgotou seus saques diários')
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
    print('\n\nDepósitos: \n')
    
    if len(deposito) == 0:
        print('Não foram realizadas movimentações!')
    else:
        for valor in deposito:
            print(f'R${valor: .2f}')
        
    print('\nSaques: \n')
    
    if len(saque) == 0:
        print('Não foram realizadas movimentações!')
    else:
        for valor in saque:
            print(f'R$ -{valor: .2f}')


while True:
    print(f'''
        \n\nEscolha uma opção: 
        
        Saldo: R${saldo_conta: .2f}     Último Depósito: R${valor_deposito: .2f}
        1 - Depósito       
        2 - Saque          
        3 - Extrato        
        q- Sair            
        '''
    )
    
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



            
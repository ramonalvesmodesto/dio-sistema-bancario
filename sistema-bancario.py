saldo_conta = 0
valor_deposito = 0
limite_saque_diario = 3
lista_deposito = []
lista_saque = []

LIMITE_SAQUE = 500

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
        
        if valor_deposito > 0:
            saldo_conta += valor_deposito
            lista_deposito.append(valor_deposito)
        else:
            print('Não é permitido depósitos de valores iguais ou menores que zero!')
            continue
    
    if entrada == '2':
        if saldo_conta == 0:
            print('Você não possui saldo!')
        elif limite_saque_diario == 0:
            print('Seu limite de saque diário foi excedido! Tente novamente amanhã!')
        else:            
            valor_saque = int(input('Digite o valor de saque: '))
            calculo_saldo = saldo_conta - valor_saque
            
            if calculo_saldo < 0:
                print('Não foi possível altorizar o saque! O valor de saque excedeu seu saldo!')
            elif valor_saque > 500:
                print(f'Não foi possível realizar o saque! Seu limite de saque é: R${LIMITE_SAQUE: .2f}')
            else:
                saldo_conta -= valor_saque
                limite_saque_diario -= 1
                lista_saque.append(valor_saque)
    
    if entrada == '3':
        print('\n\nDepósitos: \n')
        
        if len(lista_deposito) == 0:
            print('Não foram realizadas movimentações!')
        else:
            for valor in lista_deposito:
                print(f'R${valor: .2f}')
            
        print('\nSaques: \n')
        
        if len(lista_saque) == 0:
            print('Não foram realizadas movimentações!')
        else:
            for valor in lista_saque:
                print(f'R$ -{valor: .2f}')
                
    if entrada == 'q':
        break
            
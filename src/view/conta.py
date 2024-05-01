class ContaView:
    def exibir_mensagem(self, tipo_mensagem, limite=None):
        if tipo_mensagem == 1: print("\nConta criada com sucesso!!\n")
        elif tipo_mensagem == 2: print("\nNão foi possível autorizar o saque! O valor de saque excedeu seu saldo!\n")
        elif tipo_mensagem == 3: print(f"\nNão foi possível realizar o saque! Seu limite de saque é: R${limite: .2f}")
        elif tipo_mensagem == 4: print("\nNão é permitido depósitos de valores iguais ou menores que zero!\n")

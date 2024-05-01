class ContaView:
    def exibir_sucesso_nova_conta(self):
        print("\nConta criada com sucesso!!\n")

    def exibir_saque_nao_autorizado_limite(self):
        print(
                "\nNão foi possível autorizar o saque! O valor de saque excedeu seu saldo!\n"
            )
        
    def exibir_saque_nao_autorizado_limite_saque(self, limite):
        print(
                f"\nNão foi possível realizar o saque! Seu limite de saque é: R${limite: .2f}"
            )
    
    def exibir_mensagem_deposito():
        print(
                "\nNão é permitido depósitos de valores iguais ou menores que zero!\n"
            )
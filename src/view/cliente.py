import textwrap


class ClienteView:
    def exibir_mensagem(self, limite_saques, tipo_transacao):
        print(f"\nVocê excedeu o limite de {limite_saques} {tipo_transacao}s")
    
    def exibir_conta(self, conta):
        print(textwrap.dedent(
            f"""
                Nome: {conta.cliente.nome}
                C/C: {conta.numero}
                Agência: {conta.agencia}
                Saldo: {conta.saldo}
            """
        ))
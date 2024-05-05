import textwrap


class ClienteView:
    def exibir_mensagem(self, limite_saques, tipo_transacao):
        print(f"\nVocê excedeu o limite de {limite_saques} {tipo_transacao}s")

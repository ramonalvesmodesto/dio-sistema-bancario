from src.model.historico import HistoricoModel


class HistoricoView:
    def exibir_extrato(self, historico: HistoricoModel, tipo):
        print("\nExtrato: ")
        for transacao in historico.gerar_relatorio(tipo):
            print(transacao)

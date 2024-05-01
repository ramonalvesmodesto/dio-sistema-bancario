from src.model.historico import HistoricoModel


class HistoricoView():
    def exibir_extrato(lista_historico: HistoricoModel, tipo):
        print("\nExtrato: ")
        for transacao in lista_historico.gerar_relatorio(tipo):
            print(transacao)
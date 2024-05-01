from datetime import datetime
from src.model.historico import HistoricoModel
from src.model.transacao import TransacaoModel


class HistoricoController(HistoricoModel):
    def __init__(self):
        super().__init__()

    def adicionar_transacao(self, transacao: TransacaoModel):
        self.transacoes.append(transacao)

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self.transacoes:
            if tipo_transacao == str(transacao.__class__.__name__):
                yield transacao
            elif tipo_transacao == str(transacao.__class__.__name__):
                yield transacao
            elif tipo_transacao is None:
                yield transacao

    def transacoes_do_dia(self, tipo_transacao):
        data_atual = datetime.now().date()
        transacoes = []

        for transacao in self.transacoes:
            if (
                datetime.strptime(
                    transacao.data_hora_transacao, "%d-%m-%Y, %H:%M:%S"
                ).date()
                == data_atual
                and transacao.__class__.__name__ == tipo_transacao
            ):
                transacoes.append(transacao)
        return transacoes

    def __str__(self) -> str:
        return f"\nExtrato: \n{', '.join([f'{transacao}' for transacao in self.transacoes])}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.transacoes}')>"

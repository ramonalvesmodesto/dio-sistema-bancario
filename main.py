import os
from datetime import datetime
from pathlib import Path

from banco import (Banco, Cliente, Conta, ContaCorrente, ContaIterador,
                   Deposito, Endereco, Historico, PessoaFisica, Saque,
                   Transacao)
from menu import (mostrar_menu_extrato, mostrar_menu_login_cadastro,
                  mostrar_menu_movimentacao_conta)

ROOT_PATH = Path(__file__).parent


def log_transacao(func):
    def registrar(mode, args):
        with open(ROOT_PATH / "log.txt", mode, newline="") as log:
            log.write(
                f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] Função: {func.__name__.upper()} Argumentos: {args}\n'
            )

    def registro_transacao(*args, **kargs):
        if os.path.exists(ROOT_PATH / "log.txt"):
            registrar("a", args)
        else:
            registrar("w", args)
        return func(*args)

    return registro_transacao


@log_transacao
def login(banco: Banco, cpf):
    cliente = banco.buscar_cliente(cpf)

    if cliente is None:
        print("\nUsuário não encontrado\n")

    return cliente


@log_transacao
def exibir_contas_cliente(contas: Conta):
    for conta in ContaIterador(contas):
        print(conta)


@log_transacao
def exibir_contas_clientes_banco(banco: Banco):
    for cliente in banco.clientes:
        for conta in ContaIterador(cliente.contas):
            print(conta)


@log_transacao
def exibir_extrato(conta_corrente: Historico, tipo=None):
    print("\nExtrato: ")
    for transacao in conta_corrente.gerar_relatorio(tipo):
        print(transacao)


@log_transacao
def criar_conta(banco: Banco):
    nova_conta_corrente = ContaCorrente()
    nova_conta_corrente.nova_conta(banco.cliente_logado, banco.numero_conta_corrente)
    banco.numero_conta_corrente = 1

    if len(banco.cliente_logado.contas) == 0:
        banco.cliente_logado.conta_principal = nova_conta_corrente

    banco.cliente_logado.adicionar_conta(nova_conta_corrente)
    banco.conta_corrente_cliente_sessao_logada = banco.cliente_logado.conta_principal


@log_transacao
def transacao(banco: Banco, transacao: Transacao, valor):
    nova_transacao = transacao(valor)
    banco.cliente_logado.realizar_transacao(
        banco.conta_corrente_cliente_sessao_logada, nova_transacao
    )


@log_transacao
def cadastro_endereco(cliente: Cliente, logradouro, numero, estado, cidade, bairro):
    endereco = Endereco(logradouro, numero, estado, cidade, bairro)
    cliente.endereco = endereco


@log_transacao
def cadastro_cliente(banco: Banco, cpf, nome, data_nascimento):
    cliente = PessoaFisica(cpf, nome, data_nascimento)
    banco.clientes = cliente


def main():
    banco = Banco()

    while True:
        if banco.id_cliente_logado is None:
            mostrar_menu_login_cadastro()
            opcao = str(input("Escolha uma opção: "))

            if opcao == "1":
                cpf = input("Insira seu CPF: ")
                banco.cliente_logado = login(banco, cpf)
            elif opcao == "2":
                nome = input("Informe seu nome: ")
                cpf = input("Informe seu CPF: ")
                data_nascimento = input("Informe sua data de nascimento: ")
                logradouro = input("Informe seu logradouro: ")
                numero = input("Informe o número de sua casa: ")
                bairro = input("Informe seu bairro: ")
                cidade = input("Informe sua cidade: ")
                estado = input("Informe seu estado (XX): ")

                cadastro_cliente(banco, cpf, nome, data_nascimento)
                cadastro_endereco(
                    banco.cliente_logado, logradouro, numero, estado, cidade, bairro
                )
            elif opcao == "3":
                exibir_contas_clientes_banco(banco)
            elif opcao == "q":
                break

            continue

        if len(banco.cliente_logado.contas) == 0:
            opcao = str(
                input(
                    "\nVocê não possui uma conta corrente, deseja criar uma? 1 para sim, 2 para não \n=> "
                )
            )
            if opcao == "1":
                criar_conta(banco)
            else:
                continue

        mostrar_menu_movimentacao_conta(
            banco.conta_corrente_cliente_sessao_logada.saldo,
            banco.ultimo_valor_deposito,
            banco.id_cliente_logado,
        )
        entrada = str(input("Digite sua escolha: "))

        if entrada == "1":
            valor = float(
                input(
                    f"Digite o valor para {'Depósito' if entrada == '1' else 'Saque'}: "
                )
            )
            transacao(banco, Deposito, valor)
        if entrada == "2":
            valor = float(
                input(
                    f"Digite o valor para {'Depósito' if entrada == '1' else 'Saque'}: "
                )
            )
            transacao(banco, Saque, valor)
        if entrada == "3":
            mostrar_menu_extrato()
            opcao = str(input("Escolha uma opção: "))
            exibir_extrato(banco.conta_corrente_cliente_sessao_logada.historico, opcao)
        if entrada == "4":
            criar_conta(banco)
        if entrada == "5":
            exibir_contas_cliente(banco.cliente_logado.contas)
        if entrada == "q":
            banco.id_cliente_logado = None


main()

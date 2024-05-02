from src.model.transacao import TransacaoModel
from src.controller.transacao import DespositoController, SaqueController
from src.controller.banco import BancoController
from src.view.menu import (mostrar_menu_extrato, mostrar_menu_login_cadastro,
                  mostrar_menu_movimentacao_conta)

def exibir_extrato(banco: BancoController):
    tipo = None
    mostrar_menu_extrato()
    opcao = str(input("Escolha uma opção: "))

    if opcao == '1': tipo = 'DespositoController'
    elif opcao == '2': tipo = 'SaqueController'

    banco.listar_extrato(banco.cliente_logado.conta.historico, tipo)

def transacao(banco: BancoController, tipo: TransacaoModel):
    valor = float(
                input(
                    f"Digite o valor para {'Depósito' if tipo.__qualname__ == 'DespositoController' else 'Saque'}: "
                )
            )
    banco.transacao(tipo, valor)

def login(banco: BancoController):
    cpf = input("Insira seu CPF: ")
    banco.cliente_logado = banco.login(cpf)
    
def cadastrar_cliente(banco: BancoController):
    nome = input("Informe seu nome: ")
    cpf = input("Informe seu CPF: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    logradouro = input("Informe seu logradouro: ")
    numero = input("Informe o número de sua casa: ")
    bairro = input("Informe seu bairro: ")
    cidade = input("Informe sua cidade: ")
    estado = input("Informe seu estado (XX): ")
    endereco = {
        'logradouro': logradouro,
        'numero': numero,
        'estado': estado,
        'cidade': cidade,
        'bairro': bairro
    }
    
    cliente = banco.cadastro_cliente(cpf, nome, data_nascimento, endereco)
    banco.criar_conta(cliente)

def main():
    banco = BancoController()

    while True:
        if banco.id_cliente_logado is None:
            mostrar_menu_login_cadastro()
            opcao = str(input("Escolha uma opção: "))

            if opcao == "1": login(banco)
            elif opcao == "2": cadastrar_cliente(banco)
            elif opcao == "3": banco.listar_clientes()
            elif opcao == "q": break

            continue

        mostrar_menu_movimentacao_conta(banco.cliente_logado.conta.saldo, banco.id_cliente_logado)
        entrada = str(input("Digite sua escolha: "))

        if entrada == "1": transacao(banco, DespositoController)
        if entrada == "2": transacao(banco, SaqueController)
        if entrada == "3": exibir_extrato(banco)
        if entrada == "4": banco.cliente_logado.listar_conta()
        if entrada == "q": banco.id_cliente_logado = None


main()

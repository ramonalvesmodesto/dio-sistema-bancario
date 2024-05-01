import textwrap


def mostrar_menu_login_cadastro():
    menu = """
    ================ Menu ================
    [1] - Fazer login
    [2] - Realizar cadastro
    [3] - Exibir contas clientes do banco
    [q] - Sair
    =======================================
    """
    print(textwrap.dedent(menu))


def mostrar_menu_extrato():
    menu = """
    =============== Menu =================
    [1] - Depósito
    [2] - Saque
    [3] - Saque e depósito
    ======================================
    """
    print(textwrap.dedent(menu))


def mostrar_menu_movimentacao_conta(saldo, deposito, usuario):
    menu = f"""\n
    =============== Menu ===============
    Saldo: R${saldo: .2f}
    Último Depósito: R${deposito: .2f}
    Usuário: {usuario}

    [1] - \tDepósito
    [2] - \tSaque
    [3] - \tExtrato
    [4] - \tExibir Conta
    [q] - \tSair
    ======================================
    """
    print(textwrap.dedent(menu))

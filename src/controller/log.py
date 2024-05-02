from datetime import datetime
import os
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.parent


def log_banco(func):
    def registrar(mode, args):
        with open(ROOT_PATH / "log/log.txt", mode, newline="") as log:
            log.write(
                f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] Função: {func.__name__.upper()} Argumentos: {args}\n'
            )

    def registro_transacao(*args, **kargs):
        if os.path.exists(ROOT_PATH / "log/log.txt"):
            registrar("a", args)
        else:
            registrar("w", args)
        return func(*args)

    return registro_transacao

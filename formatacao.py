"""Funções para limpar e formatar dados exibidos."""

import re
from datetime import datetime


def limpar_texto(valor):
    if valor is None:
        return ""

    texto = str(valor).strip()
    return re.sub(r"\s+", " ", texto)


def limpar_inteiro(valor):
    if valor is None or str(valor).strip() == "":
        return None

    texto = re.sub(r"[^\d-]", "", str(valor))
    if re.fullmatch(r"-?\d+", texto) is None:
        raise ValueError(f"Não foi possível converter para inteiro: {valor}")
    return int(texto)


def limpar_float(valor):
    if valor is None or str(valor).strip() == "":
        return None

    texto = re.sub(r"[^\d,.-]", "", str(valor))
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    return float(texto)


def limpar_datetime(valor):
    if valor is None or str(valor).strip() == "":
        return None

    texto = str(valor).strip()
    return datetime.strptime(texto, "%d/%m/%Y")


def numero_br(valor, casas_decimais=0):
    texto = f"{valor:,.{casas_decimais}f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return texto
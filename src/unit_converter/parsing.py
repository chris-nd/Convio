"Parsing des nombres"

import re

_NUMBER = re.compile(r"[+-]?[0-9]+(?:[.,][0-9]+)?")


def parse_number(raw: str | None) -> float:
    """
    Parse un nombre à partir d'une chaîne de caractères.

    :param raw: La chaîne de caractères à parser.
    :return: Le nombre parsé.
    :rtype: float
    """
    if raw is None or not raw.strip():
        raise ValueError("Valeur manquante")
    text = raw.strip()
    if not _NUMBER.fullmatch(text):
        raise ValueError(f"Valeur invalide : {raw!r}")
    return float(text.replace(",", "."))


def parse_unit(raw: str | None, label: str) -> str:
    """
    Parse une unité à partir d'une chaîne de caractères.

    :param raw: La chaîne de caractères à parser.
    :param label: Le libellé de l'unité.
    :return: L'unité parsée.
    :rtype: str
    """
    if raw is None or not raw.strip():
        raise ValueError(f"Unité {label} manquante")
    return raw.strip()

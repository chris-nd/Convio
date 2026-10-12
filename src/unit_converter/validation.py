"Module de validation pour le convertisseur d'unités"

import math
from collections.abc import Mapping
from typing import Any


def validate_number(value: Any) -> float:
    """
    Valide et convertit une valeur en nombre à virgule flottante.

    :param value: La valeur à valider.
    :type value: Any
    :raise TypeError: Si la valeur est d'un type invalide.
    :raise ValueError: Si la valeur est trop grande.
    :raise ValueError: Si la valeur est NaN.
    :raise ValueError: Si la valeur est infinie.
    :return: Le nombre à virgule flottante validé.
    :rtype: float
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"Valeur invalide : {value!r}")
    try:
        number = float(value)
    except OverflowError as exc:  # entier gigantesque, ex. 10**400
        raise ValueError("Valeur trop grande") from exc

    if math.isnan(number):
        raise ValueError("La valeur ne doit pas être NaN")

    if math.isinf(number):
        raise ValueError("La valeur ne doit pas être infinie")

    return number


def get_factor(unit: Any, factors: Mapping[str, float]) -> float:
    """
    Récupère le facteur d'une unité donnée.

    :param unit: L'unité pour laquelle récupérer le facteur.
    :type unit: Any
    :param factors: Un dictionnaire des facteurs d'unités.
    :type factors: Mapping[str, float]
    :raise ValueError: Si l'unité est incompatible.
    :return: Le facteur de l'unité.
    :rtype: float
    """
    if not isinstance(unit, str) or unit.lower() not in factors:
        raise ValueError(
            f"Unité incompatible : {unit!r} (acceptées : {', '.join(factors)})"
        )
    return factors[unit.lower()]

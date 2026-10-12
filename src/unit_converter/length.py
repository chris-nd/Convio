"Module de convertisseur de longueur"

import math
from typing import Any

LENGTH = {
    "km": 1,
    "m": 1000,
    "dm": 10000,
    "cm": 100000,
    "mm": 1000000
}

# Fonctions utilitaires


def validate_value_and_type(value: Any) -> float:
    """
    Vérifie si une valeur est d'un type valide.

    :param value: La valeur à vérifier.
    :raise TypeError: Si le type de la valeur n'est pas supporté.
    :raise ValueError: Si la valeur est infinie.
    :raise ValueError: Si la valeur est NaN.
    :return: La valeur convertie.
    :rtype: float
    """

    if not isinstance(value, float):
            return float(value)

    if math.isnan(value):
        raise ValueError("La valeur ne doit pas être NaN")

    if math.isinf(value):
        raise ValueError("La valeur ne doit pas être infinie")

    return value


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convertit une valeur de longueur d'une unité à une autre.

    :param value: La valeur à convertir.
    :param from_unit: L'unité de départ.
    :param to_unit: L'unité d'arrivée.
    :raise ValueError: Si une des unités est incompatible.
    :raise TypeError: Si le type de la valeur n'est pas supporté.
    :raise ValueError: Si la valeur est négative.
    :raise ValueError: Si la valeur est infinie.
    :raise ValueError: Si la valeur est NaN.
    :return: La valeur convertie.
    :rtype: float
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    value = validate_value_and_type(value)

    if from_unit not in LENGTH or to_unit not in LENGTH:
        raise ValueError("Une des unités est incompatible")

    if value < 0:
        raise ValueError("La valeur ne doit pas être négative")

    return value * LENGTH[to_unit] / LENGTH[from_unit]

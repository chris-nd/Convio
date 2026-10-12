"Convertisseur d'unités de longueur"

import math

from unit_converter.validation import get_factor, validate_number

# Nombre d'unités contenues dans 1 km (pivot : le kilomètre)
UNITS_PER_KM = {"km": 1, "m": 1_000, "dm": 10_000, "cm": 100_000, "mm": 1_000_000}


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
    number = validate_number(value)
    from_factor = get_factor(from_unit, UNITS_PER_KM)
    to_factor = get_factor(to_unit, UNITS_PER_KM)

    if number < 0:
        raise ValueError("La valeur ne doit pas être négative")

    result = number * (to_factor / from_factor)

    if math.isinf(result):
        raise ValueError("Résultat trop grand pour être représenté")

    return result

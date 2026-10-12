"Tests de validation"

import pytest

from unit_converter.validation import get_factor, validate_number

FACTORS = {"a": 1, "b": 10}  # table minuscule, indépendante des vraies unités


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0.0),
        (1.5, 1.5),
        (10**6, 1e6),
        (-3, -3.0),  # le signe n'est pas son affaire : règle propre à chaque famille
    ],
)
def test_validate_number_valid(value, expected):
    """
    Teste la validation d'un nombre valide.
    """
    result = validate_number(value)
    assert isinstance(result, float)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    "value, message",
    [
        (float("nan"), "NaN"),
        (float("inf"), "infinie"),
        (float("-inf"), "infinie"),
        (10**400, "trop grande"),
        (None, "invalide"),
        ("10", "invalide"),
        (True, "invalide"),
    ],
)
def test_validate_number_invalid(value, message):
    """
    Teste la validation d'un nombre invalide.
    """
    with pytest.raises((ValueError, TypeError), match=message):
        validate_number(value)


@pytest.mark.parametrize("unit, expected", [("a", 1), ("B", 10)])
def test_get_factor_valid(unit, expected):
    """
    Teste la récupération du facteur pour une unité valide.
    """
    assert get_factor(unit, FACTORS) == expected


@pytest.mark.parametrize("unit", ["c", "", None, 5])
def test_get_factor_invalid(unit):
    """
    Teste la récupération du facteur pour une unité invalide.
    """
    with pytest.raises(ValueError, match="incompatible"):
        get_factor(unit, FACTORS)


def test_get_factor_message_lists_accepted_units():
    """
    Teste le message d'erreur lors de la récupération du
    facteur pour une unité non acceptée.
    """
    with pytest.raises(ValueError, match="acceptées : a, b"):
        get_factor("c", FACTORS)

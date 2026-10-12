"Tests de convert_length"

import pytest

from unit_converter.length import convert_length


@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
    (1, "dm", "cm", 10),
    (1, "m", "cm", 100),
    (5, "km", "m", 5000),
    (1.5, "m", "cm", 150),
    (2.5, "cm", "m", 0.025),
    (0.5, "m", "km", 0.0005),
    (1, "M", "CM", 100),
    (1, "m", "Km", 0.001),
    (1, "cM", "dm", 0.1),
    (0, "m", "cm", 0),
    (0.1, "m", "m", 0.1),
    (1e303, "mm", "mm", 1e303),  # pas de débordement intermédiaire
])
def test_convert_length_valid(value, from_unit, to_unit, expected):
    """
    Teste la conversion d'une longueur valide.
    """
    assert convert_length(value, from_unit, to_unit) == pytest.approx(expected)


# Règles propres à la longueur
@pytest.mark.parametrize("value, from_unit, to_unit, message", [
    (-1, "m", "cm", "négative"),
    (1e308, "km", "mm", "trop grand"),  # le résultat déborde
])
def test_convert_length_rules(value, from_unit, to_unit, message):
    """
    Teste les règles propres à la conversion de longueur.
    """
    with pytest.raises(ValueError, match=message):
        convert_length(value, from_unit, to_unit)


# Câblage : prouve que convert_length appelle bien les validateurs partagés
@pytest.mark.parametrize("value, from_unit, to_unit, message", [
    (float("nan"), "m", "cm", "NaN"),
    (1, "m", "foo", "incompatible"),
    (1, "foo", "m", "incompatible"),
])
def test_convert_length_uses_validators(value, from_unit, to_unit, message):
    """
    Teste l'appel aux validateurs partagés.
    """
    with pytest.raises(ValueError, match=message):
        convert_length(value, from_unit, to_unit)


# Ordre de validation : la valeur est contrôlée avant les unités
def test_convert_length_validates_value_before_units():
    """
    Teste que la valeur est contrôlée avant les unités.
    """
    with pytest.raises(TypeError, match="invalide"):
        convert_length("x", "foo", "m")

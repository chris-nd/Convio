"Module de test pour le convertisseur d'unités"

import pytest

from unit_converter.length import convert_length


# Tester les cas normaux
@pytest.mark.parametrize("value, from_unit, to_unit, expected_result", [
    (1, "dm", "cm", 10),
    (1, "m", "cm", 100),
    (5, "km", "m", 5000)
])
def test_convert_length(value, from_unit, to_unit, expected_result):
    """
    Teste la conversion de longueur d'un unité à une autre.

    :param value: La valeur à convertir
    :param from_unit: L'unité de départ
    :param to_unit: L'unité d'arrivée
    :param expected_result: Le résultat attendu
    """
    assert convert_length(value, from_unit, to_unit) == pytest.approx(expected_result)


@pytest.mark.parametrize("value, from_unit, to_unit, expected_result", [
    (1.5, "m", "cm", 150),
    (2.5, "cm", "m", 0.025),
    (0.5, "m", "km", 0.0005)
])
def test_convert_floating_length(value, from_unit, to_unit, expected_result):
    """
    Teste la conversion de longueur avec une valeur flottante.
    """
    assert convert_length(value, from_unit, to_unit) == pytest.approx(expected_result)


@pytest.mark.parametrize("value, from_unit, to_unit, expected_result", [
    (1, "M", "CM", 100),
    (1, "m", "Km", 0.001),
    (1, "cM", "dm", 0.1)
])
def test_convert_length_case_unit(value, from_unit, to_unit, expected_result):
    """
    Teste la conversion de longueur avec des unités de casse différente.
    """
    assert convert_length(value, from_unit, to_unit) == pytest.approx(expected_result)


@pytest.mark.parametrize("value, from_unit, to_unit, expected_result", [
    (1e308, "km", "mm", float('inf')),
    ("10", "m", "cm", 1000)
])
def test_convert_length_other_value_type(value, from_unit, to_unit, expected_result):
    """
    Teste la conversion de longueur avec un type de valeur différent.
    """
    assert convert_length(value, from_unit, to_unit) == pytest.approx(expected_result)


# Tester les cas limites
def test_convert_length_zero():
    """
    Teste la conversion de longueur avec une valeur de zéro.
    """
    assert convert_length(0, "m", "cm") == 0


def test_convert_length_negative():
    """
    Teste la conversion de longueur avec une valeur négative.
    """
    with pytest.raises(ValueError, match="négative"):
        convert_length(-1, "m", "cm")


def test_convert_length_same_unit():
    """
    Teste la conversion de longueur avec les mêmes unités.
    """
    assert convert_length(1, "m", "m") == 1


# Tester les cas d'erreur
@pytest.mark.parametrize("value, from_unit, to_unit", [
    (1, "kg", "cm"),
    (1, "m", "cl"),
    (1, "m", "foo")
])
def test_convert_length_invalid_or_unknown_unit(value, from_unit, to_unit):
    """
    Teste la conversion de longueur avec des unités invalides ou inconnues.
    """
    with pytest.raises(ValueError, match="incompatible"):
        convert_length(value, from_unit, to_unit)


@pytest.mark.parametrize("value, from_unit, to_unit", [
    (None, "m", "cm"),
    (None, "mm", "dm")
])
def test_convert_length_none_type(value, from_unit, to_unit):
    """
    Teste la conversion de longueur avec un type invalide.
    """
    with pytest.raises(TypeError, match="must be a string or a real number"):
        convert_length(value, from_unit, to_unit)


@pytest.mark.parametrize("value, from_unit, to_unit", [
    ("value", "m", "cm"),
    ("un", "m", "cm")
])
def test_convert_length_invalid_type(value, from_unit, to_unit):
    """
    Teste la conversion de longueur avec un type invalide.
    """
    with pytest.raises(ValueError, match="could not convert string to float"):
        convert_length(value, from_unit, to_unit)


def test_convert_length_infinite_value():
    """
    Teste la conversion de longueur avec une valeur infinie.
    """
    with pytest.raises(ValueError, match="infinie"):
        convert_length(float('inf'), "m", "cm")


def test_convert_length_nan_value():
    """
    Teste la conversion de longueur avec une valeur NaN.
    """
    with pytest.raises(ValueError, match="NaN"):
        convert_length(float('nan'), "m", "cm")

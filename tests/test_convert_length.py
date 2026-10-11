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


def test_convert_length_case_unit():
    """
    Teste la conversion de longueur avec des unités de casse différente.
    """
    assert convert_length(1, "M", "CM") == pytest.approx(100)


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
    (1, "m", "cl")
])
def test_convert_length_invalid(value, from_unit, to_unit):
    """
    Teste la conversion de longueur avec des unités invalides.
    """
    with pytest.raises(ValueError, match="incompatibles"):
        convert_length(value, from_unit, to_unit)


def test_convert_length_unknown_unit():
    """
    Teste la conversion de longueur avec une unité inconnue.
    """
    with pytest.raises(ValueError, match="inconnue"):
        convert_length(1, "m", "foo")


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

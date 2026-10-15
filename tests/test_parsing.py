"Parsing des nombres et des unités"

import pytest

from unit_converter.parsing import parse_number, parse_unit


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("5", 5.0),
        ("1,5", 1.5),
        ("1.5", 1.5),
        (" 5 ", 5.0),
        ("-3", -3.0),
    ],
)
def test_parse_number_valid(raw, expected):
    "Teste le parsing d'un nombre valide."
    assert parse_number(raw) == expected


@pytest.mark.parametrize(
    "raw",
    [
        "1_000",
        "1e3",
        "1.5.2",
        "infinity",
        "nan",
        "abc",
        "1 000",
        ".5",
        "١٢٣",
    ],
)
def test_parse_number_invalid(raw):
    "Teste le parsing d'un nombre invalide."
    with pytest.raises(ValueError, match="invalide"):
        parse_number(raw)


@pytest.mark.parametrize("raw", [None, "", "   "])
def test_parse_number_missing(raw):
    "Teste le parsing d'un nombre manquant."
    with pytest.raises(ValueError, match="manquante"):
        parse_number(raw)


@pytest.mark.parametrize("raw", [None, "", "  "])
def test_parse_unit_missing(raw):
    "Teste le parsing d'une unité manquante."
    with pytest.raises(ValueError, match="manquante"):
        parse_unit(raw, "de départ")

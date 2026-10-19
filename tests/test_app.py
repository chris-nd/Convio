"Test pour l'application Flask"

import pytest

from unit_converter.app import app


@pytest.fixture
def client():
    "Crée un client de test pour l'application Flask."
    return app.test_client()


def test_root_redirects_to_length(client):
    "Teste la redirection de la racine vers la conversion de longueur."
    response = client.get("/")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/length")


@pytest.mark.parametrize("path", ["/unknown", "/Length"])
def test_unknown_family_returns_404(client, path):
    "Teste que les familles inconnues renvoient une erreur 404."
    assert client.get(path).status_code == 404


def test_blank_form(client):
    "Teste le formulaire vide."
    response = client.get("/length")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "query, expected",
    [
        ("value=1&from=m&to=cm", "1 m = 100.0 cm"),
        ("value=1,5&from=m&to=cm", "= 150.0 cm"),  # virgule française
    ],
)
def test_valid_conversion(client, query, expected):
    "Teste les conversions valides."
    response = client.get(f"/length?{query}")
    assert response.status_code == 200
    assert expected in response.get_data(as_text=True)


@pytest.mark.parametrize(
    "query",
    [
        "value=abc&from=m&to=cm",
        "from=m&to=cm",  # valeur absente
        "value=1&from=m",  # unité absente
        "value=-1&from=m&to=cm",
        "value=nan&from=m&to=cm",
        "value=1&from=&to=cm",
        "value=1_000&from=m&to=cm",
    ],
)
def test_invalid_input_returns_400(client, query):
    "Teste les entrées invalides."
    assert client.get(f"/length?{query}").status_code == 400


def test_user_input_is_escaped(client):
    "Teste que les entrées de l'utilisateur sont échappées."
    response = client.get("/length?value=1&from=%3Cscript%3Ealert(1)%3C/script%3E&to=m")
    body = response.get_data(as_text=True)
    assert "<script>alert" not in body
    assert "&lt;script&gt;" in body

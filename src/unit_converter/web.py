"Module pour l'interface web du convertisseur d'unités"

from collections.abc import Callable, Mapping
from typing import NamedTuple

from flask import Blueprint, abort, redirect, render_template, request, url_for

from unit_converter.length import UNITS_PER_KM, convert_length
from unit_converter.parsing import parse_number, parse_unit
from unit_converter.weight import UNITS_PER_KG, convert_weight


class Family(NamedTuple):
    "Représente une famille d'unités."
    label: str
    convert: Callable[[float, str, str], float]
    units: Mapping[str, float]


FAMILIES = {
    "length": Family("longueur", convert_length, UNITS_PER_KM),
    "weight": Family("poids", convert_weight, UNITS_PER_KG),
}

bp = Blueprint("web", __name__)


@bp.route("/")
def index():
    "Gère la route de l'index."
    return redirect(url_for("web.convert", family="length"))


@bp.route("/<family>")
def convert(family: str):
    "Gère la route de conversion pour une famille d'unités."
    spec = FAMILIES.get(family)
    if spec is None:
        abort(404)

    raw_value = request.args.get("value")
    from_unit = request.args.get("from")
    to_unit = request.args.get("to")
    context = {
        "family": family,
        "label": spec.label,
        "units": list(spec.units),
        "value": raw_value,
        "from_unit": from_unit,
        "to_unit": to_unit,
    }

    if raw_value is None and from_unit is None and to_unit is None:
        return render_template("index.html", **context)  # formulaire vierge

    try:
        result = spec.convert(
            parse_number(raw_value),
            parse_unit(from_unit, "de départ"),
            parse_unit(to_unit, "d'arrivée"),
        )
    except ValueError as exc:
        return render_template("index.html", error=str(exc), **context), 400
    return render_template("index.html", result=result, **context)

"Application Flask pour la conversion d'unités"

from flask import Flask, render_template, request

from unit_converter.length import UNITS_PER_KM, convert_length
from unit_converter.parsing import parse_number, parse_unit

app = Flask(__name__)


@app.route("/")
def index():
    """
    Gestionnaire de la route principale.
    """
    raw_value = request.args.get("value")
    from_unit = request.args.get("from")
    to_unit = request.args.get("to")
    context = {
        "units": list(UNITS_PER_KM),
        "value": raw_value,
        "from_unit": from_unit,
        "to_unit": to_unit,
    }

    if raw_value is None and from_unit is None and to_unit is None:
        return render_template("index.html", **context)

    try:
        result = convert_length(
            parse_number(raw_value),
            parse_unit(from_unit, "de départ"),
            parse_unit(to_unit, "d'arrivée"),
        )
    except ValueError as exc:
        return render_template("index.html", error=str(exc), **context), 400

    return render_template("index.html", result=result, **context)

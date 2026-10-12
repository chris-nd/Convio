"Module de configuration pour l'application Flask"

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    "Gestionnaire de la route principale"
    value = request.args.get("value")
    return f"<h1>Hello, World!</h1> <p>Value: {value}</p>"


if __name__ == "__main__":
    app.run(debug=True)

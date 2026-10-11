"Module de configuration pour l'application Flask"

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    "Gestionnaire de la route principale"
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

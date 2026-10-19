"Application Flask pour la conversion d'unités"

from flask import Flask

from unit_converter.web import bp

app = Flask(__name__)
app.register_blueprint(bp)

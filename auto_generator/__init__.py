"""Auto generator Init File."""
import flask
app = flask.Flask(__name__)

import auto_generator.model
import auto_generator.views

app.config.from_object("auto_generator.config")

app.config.from_envvar('GENERATOR_SETTINGS', silent=True)

app.debug = True
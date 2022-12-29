"""Auto Generator index (main) view."""
import flask
import auto_generator

@auto_generator.app.route('/', methods=['POST', 'GET'])
def show_index():
    """Show Index Page."""
    logname = None
    if "logname" in flask.session:
        logname = flask.session['logname']
    context = {"logname": logname}
    return flask.render_template("index.html", **context)
"""Auto Generator index (main) view."""
import flask
import auto_generator
import os

@auto_generator.app.route('/uploads/<path:filename>')
def download_file(filename):
    """Download file"""
    if "logname" not in flask.session:
        return flask.abort(403)
    if not os.path.exists(auto_generator.app.config['UPLOAD_FOLDER']/filename):
        return flask.abort(404)
    return flask.send_from_directory(auto_generator.app.config['UPLOAD_FOLDER'],
                                     filename, as_attachment=True)

@auto_generator.app.route('/', methods=['POST', 'GET'])
def show_index():
    """Show Index Page."""
    logname = None
    if "logname" in flask.session:
        logname = flask.session['logname']
    context = {"logname": logname}
    return flask.render_template("index.html", **context)
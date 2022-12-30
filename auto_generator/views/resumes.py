""" Auto Generator resume view """
import flask
import auto_generator
import auto_generator.model

@auto_generator.app.route('/resumes/', methods=['POST', 'GET'])
def show_generaotr():
    logname = None
    if "logname" in flask.session:
        logname = flask.session['logname']
    context = {"logname": logname}
    return flask.render_template("resume.html", **context)
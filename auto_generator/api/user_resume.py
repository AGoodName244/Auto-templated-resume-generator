import flask
import auto_generator

@auto_generator.app.route('/api/v1/resumes/<username>')
def get_resumes(username):
    """Returns all resumes """
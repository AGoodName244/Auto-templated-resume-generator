"""
Auto Generator index (main) view
"""
import flask
import auto_generator
import auto_generator.model

@auto_generator.app.route('/accounts/login/', methods=['POST', 'GET'])
def show_login():
    """Show login page."""
    if "logname" in flask.session:
        return flask.redirect(flask.url_for('show_index'))

    if flask.request.method == 'GET':
        return flask.render_template("login.html")
    else:
        username = str(flask.request.form.get("username"))
        password = str(flask.request.form.get("password"))
        
        if username is None or password is None:
            return flask.abort(400) # can be other html error page

        connection = auto_generator.model.get_db()
        cur = connection.execute(
            "SELECT username, password "
            "FROM users "
            "WHERE username = ? ",
            (username, )
        )
        valid_account = cur.fetchone()
        if valid_account is None:
            context = {"errorMessage": "Username does not exists, please try again!"}
            return flask.render_template("login.html", **context)
            return flask.redirect(flask.url_for('show_login'))

        if (valid_account["password"] == password or
                auto_generator.model.Valid_Password(valid_account["password"], password)):
            flask.session["logname"] = username
            return flask.redirect(flask.url_for('show_index')) # can be redirected to user page
        else:
            context = {"errorMessage": "Password not correct, please try again!"}
            return flask.render_template("login.html", **context)
            return flask.abort(403) # can be other html error page
        
@auto_generator.app.route('/accounts/signup/', methods=['POST', 'GET'])
def show_signup():
    if "logname" in flask.session:
        return flask.redirect(flask.url_for('show_index'))
    
    if flask.request.method == 'GET':
        return flask.render_template("signup.html")
    else:
        username = str(flask.request.form.get("username"))
        password = str(flask.request.form.get("password"))
        
        if username is None or password is None:
            return flask.abort(400)
        connection = auto_generator.model.get_db()
        cur = connection.execute(
            "SELECT username, password "
            "FROM users "
            "WHERE username = ? ",
            (username, )
        )
        valid_account = cur.fetchone()
        if valid_account is not None:
            context = {"errorMessage": "Username already exists, please use another one"}
            return flask.render_template("signup.html", **context)
            return flask.abort(403)
        encrypt_pass = auto_generator.model.Encrypt_Password(password)
        connection.execute(
            "INSERT INTO users(username, password) "
            "VALUES (?, ?) ",
            (username, encrypt_pass)
        )
        flask.session["logname"] = username
        return flask.redirect(flask.url_for("show_index"))
    
@auto_generator.app.route('/accounts/users/<username>/', methods=['POST', 'GET'])
def show_users(username):
    """Show users account page."""
    if "logname" not in flask.session or username is None:
        return flask.redirect(flask.url_for('show_login'))
    logname = flask.session['logname']
    connection = auto_generator.model.get_db()
    cur = connection.execute(
        "SELECT profilepath "
        "FROM USERS "
        "WHERE username = ? ",
        (logname, )
    )
    user_profile = cur.fetchone()["profilepath"]
    
    cur = connection.execute(
        "SELECT filename FROM RESUME "
        "WHERE owner = ? "
        "ORDER BY created ",
        (logname, )
    )
    cur_list = cur.fetchall()
    resume_list = []
    for resume in cur_list:
        resume_list.append(resume["filename"])
    context = {"logname": logname, "user_profile": user_profile, "resume_list": resume_list}
    return flask.render_template("user_resume.html", **context)
    pass #FIXME: Writing logic for user account page
    
@auto_generator.app.route('/accounts/logout/', methods=['GET', 'POST'])
def show_logout():
    """Show logout page."""
    flask.session.clear()
    return flask.redirect(flask.url_for('show_index'))
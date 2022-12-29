"""Auto generator Model File."""
import sqlite3
import flask
import auto_generator
import hashlib
import uuid
import re

def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name.
    This is useful for building dictionaries which are then used to render a
    template.  Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

def get_db():
    """Open a new database connection.
    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    if 'sqlite_db' not in flask.g:
        db_filename = auto_generator.app.config['DATABASE_FILENAME']
        flask.g.sqlite_db = sqlite3.connect(str(db_filename))
        flask.g.sqlite_db.row_factory = dict_factory
        # Foreign keys have to be enabled per-connection.  This is an sqlite3
        # backwards compatibility thing.
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.sqlite_db

@auto_generator.app.teardown_appcontext
def close_db(error):
    """Close the database at the end of a request.
    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    assert error or not error  # Needed to avoid superfluous style error
    sqlite_db = flask.g.pop('sqlite_db', None)
    if sqlite_db is not None:
        sqlite_db.commit()
        sqlite_db.close()
        
def Encrypt_Password(password):
    """Encrypt Password."""
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])

    return password_db_string

def Valid_Password(db_password, input_password):
    """Chcek Validate Password."""
    salt = re.findall(r'\$(.*?)\$', db_password)[0]

    algorithm = 'sha512'
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + input_password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_input_string = "$".join([algorithm, salt, password_hash])

    return db_password == password_input_string
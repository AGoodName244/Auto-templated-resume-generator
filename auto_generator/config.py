"""Auto generator Config File."""
import pathlib

GENERATOR_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATABASE_FILENAME = GENERATOR_ROOT/'var'/'auto_generator.sqlite3'
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'$ python3 -c "import os; print(os.urandom(24))"'
SEESION_COOKIE_NAME = 'login'
"""Auto generator Config File."""
import pathlib

GENERATOR_ROOT = pathlib.Path(__file__).resolve().parent
DATABASE_FILENAME = GENERATOR_ROOT/'var'/'auto_generator.sqlite3'
APPLICATION_ROOT = '/'
"""Auto Generator Views Init File."""
from auto_generator.model import dict_factory
from auto_generator.model import get_db
from auto_generator.model import close_db
from auto_generator.model import Encrypt_Password
from auto_generator.model import Valid_Password
from auto_generator.views.index import show_index
from auto_generator.views.accounts import show_login
from auto_generator.views.accounts import show_logout
from auto_generator.views.accounts import show_signup
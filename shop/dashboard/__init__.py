# shop dashboard module
from flask import Blueprint

bp = Blueprint('d', __name__)

from shop.dashboard import routes

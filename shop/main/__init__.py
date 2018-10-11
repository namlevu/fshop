from flask import Blueprint

bp = Blueprint('main', __name__)

from shop.main import routes

from flask import Blueprint

bp = Blueprint('product', __name__)

from shop.product import routes

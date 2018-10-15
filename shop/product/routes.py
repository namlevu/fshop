from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required

from shop import app, db
from shop.product import bp
from shop.models import Photo, Cost, Product

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method is 'GET':
        row_no = request.args.get('r') # number of row on one page
        current_page = request.args.get('page')
        products = Product.query.all
    else:
        # TODO:
        print("method is POST. TODO ")
    return render_template('product/index.html')

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    return render_template('product/new.html')

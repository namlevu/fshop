# shop / dashboard / routes class
from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required

from shop.dashboard import bp
from shop import app, db


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
# @login_required
def index():
    return render_template('dashboard/index.html')


@bp.route('/product/')
# /d/product
# get -> select product ( one or all )
# post -> new product
# put -> update product
# delete -> delete product
def product():
    return render_template('dashboard/product/index.html')


@bp.route('/user/')
# /d/user
# get/post/put/delete
def user():
    return render_template('dashboard/user/index.html')

# /d/cost
# /d/photo

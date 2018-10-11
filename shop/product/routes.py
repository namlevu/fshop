from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required

from shop import app, db
from shop.product import bp

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('product/index.html')

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    return render_template('product/new.html')

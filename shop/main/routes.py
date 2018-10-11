from flask import render_template, redirect, url_for, flash, request, abort


from shop.main import bp
from shop import app

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
  # Do some stuff
  return render_template('home/index.html')

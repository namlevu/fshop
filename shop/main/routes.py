from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from datetime import datetime

from shop.main import bp
from shop.main.forms import InstallForm
#from shop import app, db, mongo
from shop import app, db
from shop.models import User, Photo

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
#@login_required
def index():
    u = User.query.all()[1]
    #u = "fake"
    return render_template('home/index.html', online_user=u)

@bp.route('/new_user', methods=['GET'])
def new_user():
  p = Photo(url="https://cdn3.iconfinder.com/data/icons/cat-force/256/cat_hungry.png")
  p.save()
  u = User(username="meo", photo=p)
  u.save()
  return redirect(url_for('main.index'))

@bp.route('/install', methods=['GET', 'POST'])
def install():
    form = InstallForm()
    if request.method == 'GET':
        print('GET')
    else:
        if form.validate_on_submit():
            from shop.models import User

            new_user = User(
                fullname=form.fullname.data,
                username=form.username.data,
                email=form.email.data
            )
            new_user.set_password(form.password_hash.data)
            db.session.add(new_user)
            db.session.commit()
            first_time = False
            return redirect(url_for('main.index'))

    return render_template('home/install.html', form=form)

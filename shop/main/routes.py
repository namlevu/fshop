from flask import render_template, redirect, url_for, flash, request, abort


from shop.main import bp
from shop.main.forms import InstallForm
from shop import app, first_time


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    # Do some stuff
    if first_time is True:
        # redirect to install
        print('18: is_first_time is True')
        return redirect(url_for('main.install'))
    # else
    print('21: is_first_time is False')
    return render_template('home/index.html')


@bp.route('/install', methods=['GET', 'POST'])
def install():
    global first_time
    if first_time is False:
        # redirect to index if installed
        print('29: is_first_time is False')
        return redirect(url_for('main.index'))

    form = InstallForm()

    if request.method == 'GET':
        print('GET')
    else:
        if form.validate_on_submit():
            from shop.models import User
            from shop import db
            
            new_user = User(
                fullname=form.fullname.data,
                username=form.username.data,
                email=form.email.data,
                password_hash=form.password_hash.data
            )
            db.session.add(new_user)
            db.session.commit()
            first_time = False
            return redirect(url_for('main.index'))

    return render_template('home/install.html', form=form)

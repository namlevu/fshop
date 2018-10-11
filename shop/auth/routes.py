from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, current_user, login_required

from shop.auth.forms import LoginForm, ChangePasswordForm
from shop.auth import bp
from shop.models import User
from shop import db

@bp.route('/login', methods=['GET', 'POST'])
def login():
  print('Login start')
  if current_user.is_authenticated:
    print('Login current_user.is_authenticated')
    return redirect(url_for('main.index'))
  form = LoginForm()
  if form.validate_on_submit():
    print('Login form.validate_on_submit')
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      print('Login Invalid username or password')
      return redirect(url_for('auth.login'))
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('main.index'))

  return render_template('home/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.index'))

@bp.route('/changepass', methods=['GET', 'POST'])
@login_required
def changepass():
  form = ChangePasswordForm()
  error_msg = None
  if form.validate_on_submit():
    user = User.query.filter_by(id=current_user.id).first()
    if user.check_password(form.old_password.data):
      if form.new_password.data == form.password_repeat.data:
        user.set_password(form.new_password.data)
        db.session.commit()

        error_msg = 'Password changed successful.'
      else:
        error_msg = 'Password repeat is not same with new password.'
    else:
      error_msg = 'Old password is invalid.'

  return render_template('home/changepass.html', msg=error_msg, form=form)

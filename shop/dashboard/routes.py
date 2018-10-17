# shop / dashboard / routes class
from flask import render_template, redirect, url_for, flash, request, jsonify
#from flask_login import current_user, login_required

from shop.dashboard import bp
from shop import app, db


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
# @login_required
def index():
    return render_template('dashboard/index.html')


@bp.route('/product')
# /d/product
# get -> select product ( one or all )
# post -> new product
# put -> update product
# delete -> delete product
def product():
    return render_template('dashboard/product/index.html')


@bp.route('/user/',methods=['GET', 'POST', 'PATCH', 'DELETE'])
# /d/user
# get/post/put/delete
def user():
    if request.method == 'POST':
        if data.get('name', None) is not None and data.get('email', None) is not None:
            msg=data.get('name', None)
            return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
        msg="POST-will create new user"
    elif request.method == 'GET':
        query = request.args#ImmutableMultiDict
        msg=query
    elif request.method == 'PATCH':
        msg='PATCH-will update infor of user'
    elif request.method == 'DELETE':
        msg='DELETE-will delete user'
    else:
        msg='ERROR'

    return render_template('dashboard/user/index.html', msg=msg)

# /d/cost
# /d/photo

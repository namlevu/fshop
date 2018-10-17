from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
db = MongoEngine()

app = Flask(__name__)

app.secret_key = b'www.namvl.com@ln'
app.config.from_object(Config)
db.init_app(app)

login = LoginManager(app)
login.login_view = 'auth.login'

#global first_time
#first_time = True
# -------------------------------------------------
from shop.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
# -------------------------------------------------
from shop.product import bp as prod_bp
app.register_blueprint(prod_bp, url_prefix='/product')
# -------------------------------------------------
from shop.main import bp as main_bp
app.register_blueprint(main_bp)
# -------------------------------------------------
from shop.dashboard import bp as admin_bp
app.register_blueprint(admin_bp, url_prefix='/d')

from shop import models

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.secret_key = b'www.namvl.com@ln'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
global first_time
first_time = True
from shop.main import bp as main_bp
app.register_blueprint(main_bp)


from shop import models

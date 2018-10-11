from flask import Flask
from config import Config

app = Flask(__name__)

app.secret_key = b'www.namvl.com@ln'
app.config.from_object(Config)

from shop.main import bp as main_bp
app.register_blueprint(main_bp)

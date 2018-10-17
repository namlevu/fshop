# shop.models
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin

from shop import db
#from shop import login

class Photo(db.EmbeddedDocument):
  url = db.StringField()

class User(db.EmbeddedDocument):
  username = db.StringField()
  photo = db.EmbeddedDocumentField(Photo)
  fullname = db.StringField()
  email = db.StringField()
  password_hash = db.StringField()
  disabled = db.BooleanField()

class Cost(db.EmbeddedDocument):
  amount = db.IntField()
  reason = db.StringField()
  created_by = db.EmbeddedDocumentField(User)
  created_at = db.DateTimeField()

class Product(db.Document):
  name = db.StringField()
  category = db.StringField()
  uuid = db.StringField()
  brand = db.StringField()
  photos = db.EmbeddedDocumentListField(Photo)
  costs = db.EmbeddedDocumentListField(Cost)
  sale_price = db.IntField()
  created_by = db.EmbeddedDocumentField(User)
  created_at = db.DateTimeField()
  updated_by = db.EmbeddedDocumentField(User)
  updated_at = db.DateTimeField()
  history = db.StringField()
  note = db.StringField()


"""
class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    disabled = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Admin {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    disabled = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
      return User.query.get(int(id))


class Product(db.Model):
    uuid = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(128))
    brand = db.Column(db.String(128))
    category = db.Column(db.String(128))
    photos = db.relationship("Photo")
    costs = db.relationship("Photo")
    sale_price = db.Column(db.Integer)
    created_by = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    updated_at = db.Column(db.DateTime)
    history = db.Column(db.Text)
    note = db.Column(db.Text)


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(32), db.ForeignKey('product.uuid'))
    url = db.Column(db.String(256))


class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(32), db.ForeignKey('product.uuid'))
    amount = db.Column(db.Integer)
    reason = db.Column(db.String(256))
    created_at = db.Column(db.DateTime)
    note = db.Column(db.Text)
"""

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import NotFound
from flask import url_for, current_app
# from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from .helpers import args_from_url
from .errors import ValidationError

mongo = PyMongo()


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True)
#     password_hash = db.Column(db.String(128))

#     @property
#     def password(self):
#         raise AttributeError('password is not a readable attribute')

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)

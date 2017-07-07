from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import NotFound
from flask import url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from .helpers import args_from_url
from .errors import ValidationError

db = SQLAlchemy()


class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    properties = db.Column(db.Text, default='{}')

    def get_url(self):
        return url_for('api.get_server', id=self.id, _external=True)

    def import_data(self, data):
        try:
            self.name = data['name']
            self.properties = str(data['properties'])
        except KeyError as e:
            raise ValidationError('Invalid server: missing ' + e.args[0])
        return self

    def export_data(self):
        return {'self_url': self.get_url(),
                'name': self.name,
                'properties': self.properties}


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# coding=utf-8

from src.config.database import db
from marshmallow import Schema, fields

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    roles = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True, server_default='1')

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active


class UserSchema(Schema):
    id = fields.Number()
    email = fields.Str()
    roles = fields.Str()
    is_active = fields.Bool()

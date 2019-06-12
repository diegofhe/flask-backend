# coding=utf-8

from src.database import db
from marshmallow import Schema, fields

class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        print('initialize')
        print(self)

    def __repr__(self):
        return '<User %r>' % self.username
        print('noo')

class AppUserSchema(Schema):
    id = fields.Number()
    username = fields.Str()
    email = fields.Str()
   
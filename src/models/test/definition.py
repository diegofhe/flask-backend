# coding=utf-8

from src.config.database import db
from marshmallow import Schema, fields

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class TestSchema(Schema):
    id = fields.Number()
    username = fields.Str()
    email = fields.Str()
   
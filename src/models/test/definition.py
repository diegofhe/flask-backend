# coding=utf-8

from src.config.database import db
from marshmallow import Schema, fields

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name

class TestSchema(Schema):
    id = fields.Number()
    name = fields.Str()

   
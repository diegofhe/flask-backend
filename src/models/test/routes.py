# coding=utf-8

from flask import jsonify, Blueprint
from src.models.test.definition import Test, TestSchema
from src.config.database import db

rootBase = '/test/'
test = Blueprint('test', __name__)

@test.route(f'{rootBase}makeDummy')
def makeDummy():
    test = Test('diego', 'diegofhrg@gmail.com')
    print(test)
    db.session.add(test)
    db.session.commit()
    return "hello flask";

@test.route(f'{rootBase}', methods=['GET'])
def getAll():
    schema = TestSchema(many = True)
    elements = schema.dump(db.session.query(Test).all())
    return jsonify(elements.data);

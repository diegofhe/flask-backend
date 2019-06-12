# coding=utf-8

from flask import Flask, jsonify, request, Blueprint
from src.models.test.definition import Test
from src.database import db

rootBase = '/test/'
test = Blueprint('test', __name__)

@test.route(f'{rootBase}makeDummy')
def makeDummy():
    test = Test('diego', 'diegofhrg@gmail.com')
    print(test);
    db.session.add(test);
    return "hello flask";

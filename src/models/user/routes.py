# coding=utf-8

from flask import Blueprint
from src.models.user.definition import User
from src.config.database import db
from src.config.prestorian import guard
rootBase = '/Users/'
users = Blueprint('users', __name__)

@users.route(f'{rootBase}makeDummy')
def makeDummy():
    db.session.add(User(
        email='user@gmail.com',
        password=guard.encrypt_password('abides'),
    ))
    db.session.add(User(
        email='admin@gmail.com',
        password=guard.encrypt_password('calmerthanyouare'),
        roles='admin'
    ))
    db.session.add(User(
        email='operator@gmail.com',
        password=guard.encrypt_password('iamthewalrus'),
        roles='operator'
    ))
    db.session.add(User(
        email='many@gmail.com',
        password=guard.encrypt_password('andthorough'),
        roles='operator,admin'
    ))
    db.session.commit()
    return "dummy users created";

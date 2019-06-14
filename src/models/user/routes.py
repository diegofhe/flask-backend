# coding=utf-8

from flask import Blueprint, request, jsonify
import flask_praetorian
from src.models.user.definition import User, UserSchema
from src.config.database import db
from src.config.prestorian import guard

rootBase = '/Users'
users = Blueprint('users', __name__)


@users.route(f'{rootBase}/makeDummy')
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


@users.route(f'{rootBase}/login', methods=['POST'])
def login():
    req = request.get_json(force=True)
    email = req.get('email', None)
    password = req.get('password', None)
    user_queried = guard.authenticate(email, password)
    token = guard.encode_jwt_token(user_queried);
    # include user
    schema = UserSchema(many=False)
    user_dumped = schema.dump(user_queried)
    result = {'access_token': token, 'user': user_dumped.data}
    return (jsonify(result), 200)


@users.route(f'{rootBase}/signin', methods=['POST'])
def signin():
    req = request.get_json(force=True)
    email = req.get('email', None)
    password = req.get('password', None)
    user_found = db.session.query(User).filter_by(email=email).first()
    if user_found is not None:
        return jsonify({"error": "EmailAlreadyExist", "message": "The email is already taken", "status_code": "303"}), 303

    db.session.add(User(
        email=email,
        password=guard.encrypt_password(password),
        roles=''
    ))
    db.session.commit()
    return jsonify("User Signed Successfully"), 200




@users.route(f'{rootBase}/required')
@flask_praetorian.auth_required
def required():
    print('required in!!')
    return jsonify([1, 2, 3])

# coding=utf-8

from flask import Blueprint, request, jsonify, render_template
import flask_praetorian
import os
import pendulum

from src.models.user.definition import User, UserSchema
from src.config.database import db
from src.config.prestorian import guard
from flask_mail import Message
from src.config.mailer import mail
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
    msg = Message("Welcome to REal Dashboard", recipients=[email])
    msg.html = render_template('welcome_email.html', name = email, link = os.environ.get('FRONT_END_URL') )
    mail.send(msg)
    return jsonify("User Signed Successfully"), 200

@users.route(f'{rootBase}/sendPasswordRecoveryMail', methods=['POST'])
def send_password_recovery_mail():
    TOKEN_LIFESPAN = 15  # minutes
    req = request.get_json(force=True)
    email = req.get('email', None)
    user_found = db.session.query(User).filter_by(email=email).first()
    if user_found is None:
        return jsonify({"error": "EmailNotRegistered", "message": "The email is not found", "status_code": "404"}), 404
    temp_token = guard.encode_jwt_token(user_found, pendulum.duration(minutes=TOKEN_LIFESPAN));
    msg = Message("Password reset REal Dashboard", recipients=[email])
    link = os.environ.get('FRONT_END_URL') + '/public/account/recover-password/' + temp_token
    msg.html = render_template('password_reset.html', name=email, link=link, minutes=TOKEN_LIFESPAN)
    mail.send(msg)

    return jsonify("Email sent!"), 200

@users.route(f'{rootBase}/resetPassword', methods=['POST'])
def reset_password():
    req = request.get_json(force=True)
    password = req.get('password', None)
    token = guard.read_token_from_header()
    token_dict = guard.extract_jwt_token(token)
    user_id = token_dict['id']
    user_found = db.session.query(User).get(50)
    if user_found is None:
        return jsonify({"error": "UserNotFound", "message": "The user no longer exist in the app", "status_code": "404"}), 404
    user_found.password = guard.encrypt_password(password)
    db.session.commit()

    return jsonify("Password Updated"), 200


@users.route(f'{rootBase}/required')
@flask_praetorian.auth_required
def required():
    print('required in!!')
    return jsonify([1, 2, 3])

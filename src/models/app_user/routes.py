# coding=utf-8

from flask import Flask, jsonify, request, Blueprint
from src.models.app_user.definition import AppUser, AppUserSchema
from src.database import db

rootBase = '/appUser/'
app_users = Blueprint('app_users', __name__)

@app_users.route(f'{rootBase}', methods = ['GET'])
def index():
    return "hello flask"

@app_users.route(f'{rootBase}makeDummy')
def makeDummy():
    appuser = AppUser("diego", "diegofhrg@gmail.com")
    print(appuser);
    db.session.add(appUser);
    return "hello flask";

@app_users.route(f'{rootBase}', methods = ['POST'])
def postUser():
    return "hello flask"
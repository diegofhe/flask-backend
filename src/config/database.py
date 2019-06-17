# coding=utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setDB(app):
    global db
    db_url = 'localhost:3306'
    db_name = 'local'
    db_user = 'root'
    db_password = '@cuarroro00'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{db_user}:{db_password}@{db_url}/{db_name}'

    db.init_app(app)
# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def setDB(app):
    global db
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_url = os.environ.get('DB_URL')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}'

    db.init_app(app)
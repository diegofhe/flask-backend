# coding=utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setDB(app):
    print(app)
    global db
    print('setDB')
    db_url = 'localhost:3306'
    db_name = 'local'
    db_user = 'root'
    db_password = '@cuarroro00'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:@cuarroro00@localhost:3306/local'

    db.init_app(app)
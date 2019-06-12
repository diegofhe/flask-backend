# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.database import setDB
from src.models.app_user.routes import app_users
from src.models.test.routes import test


app = Flask(__name__)
setDB(app)
app.register_blueprint(app_users)
app.register_blueprint(test)



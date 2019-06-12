# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.app_user.routes import app_users
from src.database import setDB
from flask_migrate import Migrate


app = Flask(__name__)
setDB(app)
app.register_blueprint(app_users)



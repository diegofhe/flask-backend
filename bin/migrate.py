#https://flask-migrate.readthedocs.io/en/latest/
#
#from base root directory
#pipenv shell
#python -m bin.migrate db init
#python -m bin.migrate  db migrate
#python -m bin.migrate  db upgrade

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.database import db


app = Flask(__name__)

db_url = 'localhost:3306'
db_name = 'local'
db_user = 'root'
db_password = '@cuarroro00'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:@cuarroro00@localhost:3306/local'

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from src.models.app_user.definition import AppUser
from src.models.test.definition import Test


if __name__ == '__main__':
    manager.run()
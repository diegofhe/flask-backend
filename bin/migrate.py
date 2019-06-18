# https://flask-migrate.readthedocs.io/en/latest/
#
# from base root directory
# set all variables to connect to db
# python -m bin.migrate db init
# python -m bin.migrate  db migrate
# python -m bin.migrate  db upgrade

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.config.database import db
from src.main import app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from src.models.test.definition import Test
from src.models.user.definition import User

if __name__ == '__main__':
    manager.run()

# coding=utf-8
# (set all variables needed to connect to database) & python -m bin.seed seed_models
#
from flask_script import Manager

from src.main import app
from src.config.database import db
from src.config.prestorian import guard

from src.models.user.definition import User

manager = Manager(app)

def seed_users():
    db.session.add(User(
        email='admin@gmail.com',
        password=guard.encrypt_password('password'),
        roles='Administrator'
    ))
    db.session.add(User(
        email='user@gmail.com',
        password=guard.encrypt_password('password'),
        roles=''
    ))
    db.session.commit()

@manager.command
def seed_models():
    seed_users()


if __name__ == "__main__":
    manager.run()
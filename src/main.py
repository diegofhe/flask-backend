# coding=utf-8

from flask import Flask

from src.config.database import setDB
from src.config.prestorian import setPrestorian
from src.config.mailer import setMail

from src.models.user.routes import users
from src.models.test.routes import test

app = Flask(__name__)
app.config['DEBUG'] = True

setDB(app)
setPrestorian(app)
setMail(app)

# register blue prints
app.register_blueprint(users)
app.register_blueprint(test)


if __name__ == '__main__':
    app.run()

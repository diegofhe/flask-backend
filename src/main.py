# coding=utf-8

from flask import Flask, request, jsonify
from src.config.database import setDB
from src.config.prestorian import setPrestorian, guard

from src.models.user.routes import users
from src.models.test.routes import test

app = Flask(__name__)
app.config['DEBUG'] = True

setDB(app)
setPrestorian(app)

#register blue prints
app.register_blueprint(users)
app.register_blueprint(test)

# Add users for the example
if __name__ == '__main__':
    app.run()

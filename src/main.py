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


@app.route('/login', methods=['POST'])
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.

    .. example::
       $ curl http://localhost:5000/login -X POST \
         -d '{"username":"Walter","password":"calmerthanyouare"}'
    """
    req = request.get_json(force=True)
    email = req.get('email', None)
    password = req.get('password', None)
    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return (jsonify(ret), 200)

# Add users for the example
if __name__ == '__main__':
    app.run()

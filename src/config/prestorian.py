import flask_praetorian
import flask_cors
from src.models.user.definition import User
guard = flask_praetorian.Praetorian()
cors = flask_cors.CORS()


# praetorian
def setPrestorian(app):
    app.config['SECRET_KEY'] = 'top secret'
    app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
    app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}
    guard.init_app(app, User)
    cors.init_app(app)
    guard.init_app(app, User)
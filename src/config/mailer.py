from flask_mail import Mail, Message
import os

# flask_mail
mail =  Mail()

def setMail(app):
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    mail.init_app(app)

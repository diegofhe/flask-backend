from flask_mail import Mail, Message

# flask_mail
mail =  Mail()


def setMail(app):
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'exampleluphole@gmail.com'  # enter your email here
    app.config['MAIL_DEFAULT_SENDER'] = 'exampleluphole@gmail.com'  # enter your email here
    app.config['MAIL_PASSWORD'] = '123password'  # enter your password here
    mail.init_app(app)

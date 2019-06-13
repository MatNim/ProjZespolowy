import os
from flask import Flask
from pony.orm import *
from flask_login import LoginManager
from pony.flask import Pony
from flask_mail import Message, Mail

app = Flask(__name__)
Pony(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db = Database()
from ProjZespolowy import routes
login_manager = LoginManager(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'flaalf0123@gmail.com'
app.config['MAIL_PASSWORD'] = 'flaflahas'

mail = Mail(app)

@login_manager.user_loader
def load_user(user_id):
    return db.Osoba.get(id=user_id)



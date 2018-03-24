
#********************************** IMPORTS  **********************************
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask.ext.login import LoginManager



#********************************** CONFIGURATIONS  **********************************
app = Flask(__name__)
app.secret_key = 'super-duper-secret-key'
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

if __name__ == '__main__':
    app.run()

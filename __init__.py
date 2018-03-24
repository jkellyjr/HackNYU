#********************************** IMPORTS  **********************************
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask.ext.login import LoginManager



#********************************** CONFIGURATIONS  **********************************
app = Flask(__name__)
app.secret_key = 'super-duper-secret-key'
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:5000/hack'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#********************************** INIT  **********************************
from .models import User

@app.cli.command('initdb')
def initdb_command():
    """Reinitializes the database"""
    db.drop_all()
    db.create_all()
    db.session.commit()

    print('Created Database')


if __name__ == '__main__':
    app.run()



## KNOWN ISSUES
# 1.) User::signUp allows multiple radio button clicks

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
    # crisis = Crisis('Panic Attack')
    #db.session.add(crisis)
    # step1 = Steps('Breathing: Try controlling your breathing inhaling for 4 seconds and exhaling for 7 seconds.', crisis.id)
    # step2 = Steps('Visualization: Close your eyes and try to picture yourself in a comforting place or a relaxing environment where you feel safe.', crisis.id)
    # step3 = Steps('Grounding: Use your senses to try and "come back to the moment". Focus on the texture of your clothes or something you can smell to re-ground yourself.', crisis.id)
    # step4 = Steps('Meditation: Try and combine all of these to meditate. Focus your mind on a place or object to achieve a clear and calm state.', crisis.id)
    db.session.add(User('Bob', 'Smith', 'p@gmail.com', '1111111111', generate_password_hash('123'), 'patient'))
    db.session.add(User('Carol', 'Smith', 't@gmail.com', '1111111111', generate_password_hash('123'), 'therapist'))
    db.session.commit()

    print('Created Database')


if __name__ == '__main__':
    app.run()

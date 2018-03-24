#********************************** IMPORTS  **********************************
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import LoginManager



#********************************** CONFIGURATIONS  **********************************
app = Flask(__name__)
app.secret_key = 'super-duper-secret-key'
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hack.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#********************************** INIT  **********************************
<<<<<<< HEAD
from .models import User
=======
from .models import User, Crisis, Step
>>>>>>> d96059d5856ea8ccd73c72de47e355b355434dd5

@app.cli.command('initdb')
def initdb_command():
    """Reinitializes the database"""
    db.drop_all()
    db.create_all()
<<<<<<< HEAD
=======

    user1 = User('Bob', 'Smith', 'p@gmail.com', '4074219805', generate_password_hash('123'), 'patient')
    user2 = User('Carol', 'Smith', 't@gmail.com', '4074219805', generate_password_hash('123'), 'therapist')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    crisis = Crisis('Panic Attack', 'panic_attack')
    db.session.add(crisis)
    db.session.commit()

    step1 = Step('Breathing: Try controlling your breathing inhaling for 4 seconds and exhaling for 7 seconds.', 'https://www.nytimes.com/2016/11/09/well/mind/breathe-exhale-repeat-the-benefits-of-controlled-breathing.html', crisis.id)
    step2 = Step('Visualization: Close your eyes and try to picture yourself in a comforting place or a relaxing environment where you feel safe.', 'https://www.mentalhelp.net/articles/visualization-and-guided-imagery-techniques-for-stress-reduction/', crisis.id)
    step3 = Step('Grounding: Use your senses to try and "come back to the moment". Focus on the texture of your clothes or something you can smell to re-ground yourself.', 'https://www.livingwell.org.au/well-being/mental-health/grounding-exercises/', crisis.id)
    step4 = Step('Meditation: Try and combine all of these to meditate. Focus your mind on a place or object to achieve a clear and calm state.', 'https://www.gaiam.com/blogs/discover/meditation-101-techniques-benefits-and-a-beginner-s-how-to', crisis.id)

    db.session.add(step1)
    db.session.add(step2)
    db.session.add(step3)
    db.session.add(step4)

>>>>>>> d96059d5856ea8ccd73c72de47e355b355434dd5
    db.session.commit()

    print('Created Database')


if __name__ == '__main__':
    app.run()

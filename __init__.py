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
from .models import User, Crisis, Step
<<<<<<< HEAD

=======
>>>>>>> 11ff0789e39dc5379fc29dd0fb440d16fe427893

@app.cli.command('initdb')
def initdb_command():
    """Reinitializes the database"""
    db.drop_all()
    db.create_all()
<<<<<<< HEAD

=======
>>>>>>> 11ff0789e39dc5379fc29dd0fb440d16fe427893

    user1 = User('Bob', 'Smith', 'a@gmail.com', '4074219805', generate_password_hash('123'), 'patient')
    user2 = User('Carol', 'Stevens', 'b@gmail.com', '4074219805', generate_password_hash('123'), 'therapist')
    user3 = User('Anna','Martin','c@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user4 = User('Daniel','Rutgers','d@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user5 = User('Frank','Lorris','e@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user6 = User('Nancy','Conway','f@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user7 = User('Morgan','Wilson','g@gmail.com','4074219805', generate_password_hash('123'),'therapist')
    user8 = User('Jake','Holden','h@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user9 = User('Claire','Morris','i@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user10 = User('Stan','Thomas','j@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user11 = User('Grant','Black','k@gmail.com','4074219805', generate_password_hash('123'),'therapist')
    user12 = User('Michael','Stanley','l@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user13 = User('Kat','Eckard','m@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user14 = User('Jack','Hoffman','n@gmail.com','4074219805', generate_password_hash('123'),'patient')
    user15 = User('Ruger','Emmet','o@gmail.com','4074219805', generate_password_hash('123'),'therapist')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)
    db.session.add(user11)
    db.session.add(user12)
    db.session.add(user13)
    db.session.add(user14)
    db.session.add(user15)
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

    db.session.commit()

    print('Created Database')


if __name__ == '__main__':
    app.run()

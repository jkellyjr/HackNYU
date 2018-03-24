#********************************** IMPORTS  **********************************
from hack import db
from flask.ext.login import UserMixin

#**********************************  ASSOCIATION TABLES  **********************************
# remember_topics = db.Table('remember_topics',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
#     db.Column('rember_topic_id', db.Integer, db.ForeignKey('rember_topic.id'))
# )
medicalPairs = db.Table('medicalPairs',
    db.Column('patient_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('therapist_id', db.Integer, db.ForeignKey('user.id'))
)

pairs = db.Table('pairs',
    db.Column('patient_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('therapist_id', db.Integer, db.ForeignKey('user.id'))
)


#********************************** MODELS  **********************************
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    email = db.Column(db.String(60), unique = True)
    phone = db.Column(db.String(15))
    password = db.Column(db.String(300))
    user_role = db.Column(db.String(15))

    remember_topics = db.relationship('RememberTopic', backref=db.backref('User', lazy = True))
    matchedPairs = db.relationship('User', secondary = medicalPairs, primaryjoin = (medicalPairs.c.patient_id == id),
                    secondaryjoin = (medicalPairs.c.therapist_id == id), backref = db.backref('medicalPairs', lazy = 'dynamic'), lazy = 'dynamic')

    therapist = db.relationship('User', secondary = pairs, primaryjoin = (pairs.c.patient_id == id),
                    secondaryjoin = (pairs.c.therapist_id == id), backref = db.backref('pairs', lazy = 'dynamic'),
                    lazy = 'dynamic')


    def __init__(self, first_name, last_name, email, phone, password, user_role):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        self.user_role = user_role

    def __repr__(self):
        return '<User: %r %r>' %(self.first_name, self.last_name)




class RememberTopic(db.Model):
    __tablename__ = 'remeber_topic'

    id = db.Column(db.Integer, unique = True, primary_key = True)
    title = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, user_id):
        self.title = title
        self.user_id = user_id

    def __repr__(self):
        return '<RememberTopic: %r>' %(self.title)

class Crisis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    #crisis_id = db.Column(db.Integer, db.ForeignKey('crisis.id'), nullable=False)
    steps = db.relationship('Step', backref=db.backref('Crisis', lazy=True))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Crisis: %r>' %(self.title)

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(90), nullable=False)
    step_id = db.Column(db.Integer, db.ForeignKey('crisis.id'), nullable=False)
    url = db.Column(db.String(90), nullable=False)

    def __init__(self, text, crisis_id):
        self.text = text
        self.crisis_id = crisis_id

    def __repr__(self):
        return '<step: %r>' %(self.text)

#********************************** IMPORTS  **********************************
from hack import db
from flask_login import UserMixin

#**********************************  ASSOCIATION TABLES  **********************************
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
    last_seen = db.Column(db.Date)

    day_info = db.relationship('DayInfo', backref=db.backref('User', lazy = True))
    remember_topics = db.relationship('RememberTopic', backref=db.backref('User', lazy = True))
    therapist = db.relationship('User', secondary = pairs, primaryjoin = (pairs.c.patient_id == id),
                    secondaryjoin = (pairs.c.therapist_id == id), backref = db.backref('pairs', lazy = 'dynamic'), lazy = 'dynamic')

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



class DayInfo(db.Model):
    __tablename__ = 'day_info'

    id = db.Column(db.Integer, unique = True, primary_key =True)
    date = db.Column(db.Date, nullable = False)
    topic_and_responces = db.Column(db.String(5000))
    day_rate = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, date, topic_and_responces, day_rate, user_id):
        self.date = date
        self.topic_and_responces = topic_and_responces
        self.day_rate = day_rate
        self.user_id = user_id

    def __repr__(self):
        return '<DayRate: %r, rate: %r>' % (self.date, self.day_rate)



class Crisis(db.Model):
    __tablename__ = 'crisis'

    id = db.Column(db.Integer, unique = True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50))
    steps = db.relationship('Step', backref=db.backref('Crisis', lazy=True))

    def __init__(self, title, type):
        self.title = title
        self.type = type

    def __repr__(self):
        return '<Crisis: %r>' %(self.title)


class Step(db.Model):
    __tablename__ = 'step'

    id = db.Column(db.Integer, unique = True, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(200))
    crisis_id = db.Column(db.Integer, db.ForeignKey('crisis.id'))


    def __init__(self, text, url, crisis_id):
        self.text = text
        self.url = url
        self.crisis_id = crisis_id

    def __repr__(self):
        return '<Step: %r>' % (self.text)

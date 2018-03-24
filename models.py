#********************************** IMPORTS  **********************************
from hack import db
from flask.ext.login import UserMixin

#**********************************  ASSOCIATION TABLES  **********************************
# remember_topics = db.Table('remember_topics',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
#     db.Column('rember_topic_id', db.Integer, db.ForeignKey('rember_topic.id'))
# )

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

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<RememberTopic: %r>' %(self.title)
# class Crisis(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), nullable=False)
#     steps = db.relationship('Step', backref='Crisis', lazy=True)

#     def __init__(self, title):
#         self.title = title

#     def __repr__(self):
#         return '<Crisis: %r>' %(self.title)

# class Step(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), nullable=False)
#     step_id = db.Column(db.Integer, db.ForeignKey('step.id'), nullable=False)

#     def __init__(self, title):
#         self.title = title

#     def __repr__(self):
#         return '<Step: %r>' %(self.title)

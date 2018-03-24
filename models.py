#********************************** IMPORTS  **********************************
from hack import db
from flask.ext.login import UserMixin

#**********************************  ASSOCIATION TABLES  **********************************

#********************************** MODELS  **********************************
class User(db.Model, UserMixin):
    __tablename = 'user'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    email = db.Column(db.String(60), unique = True)
    password = db.Column(db.String(300))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User: %r %r' %(self.first_name, self.last_name)

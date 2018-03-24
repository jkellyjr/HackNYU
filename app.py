#********************************** IMPORTS  **********************************
from hack import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, g
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, RememberTopic
from .forms import LoginForm, SignUpForm


#********************************** HELPERS  **********************************
@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        db.session.add(g.user)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#********************************** VIEWS  **********************************
@app.route('/', methods = ['GET'])
@login_required
def home():
    user = User.query.filter_by(id = g.user.id).first()
    print("rolllie: " + user.user_role)

    if user.user_role == 'patient':
        headers = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return render_template('index_patient.html', user = g.user, table_head = headers, remeber_topics = user.remember_topics)
    else:
        return render_template('index.html', user = g.user)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if g.user is not None and g.user.is_authenticated:
        flash('You are already signed in')
        return redirect(url_for('home'))

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        print("post request made")
        user = User.query.filter_by(email = request.form['email']).first()
        if user == None:
            flash('Invalid username provided')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, request.form['password']):
            flash('Invalid password provided')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
    else:
        return render_template('login.html', form = form)


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email = request.form['email']).first()
        if user != None:
            flash('Username already exists')
            return redirect(url_for('signup'))
        elif request.form['password'] != request.form['confirm_password']:
            flash('The passwords do not match')
            return redirect(url_for('signup'))
        else:
            user = User(request.form['first_name'], request.form['last_name'], request.form['email'], request.form['phone'], generate_password_hash(request.form['password']), request.form['choice1'])
            print(user)
            db.session.add(user)
            db.session.commit()
        if user != None:
                login_user(user)
        return redirect(url_for('home'))
    else:
        return render_template('signup.html', form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/new_topic', methods = ['GET', 'POST'])
def add_remeber_topic():
    if request.method == 'POST':
        topic = RememberTopic(request.form('title'))
        print("new topic: " + topic)

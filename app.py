#********************************** IMPORTS  **********************************
from hack import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, g
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from .models import User
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

# Add a user to the database
def add_user(username, password, confirm_password, user_role, return_fun):
    user = User.query.filter_by(username = username).first()

    if user != None:
        flash('Username already exists')
        return redirect(url_for(return_fun))
    elif password != confirm_password:
        flash('The passwords do not match')
        return redirect(url_for(return_fun))
    else:
        user = User(username, generate_password_hash(password), user_role)
        db.session.add(user)
        db.session.commit()
        return user


#********************************** VIEWS  **********************************
@app.route('/', methods = ['GET'])
@login_required
def home():
    return 'hello world'


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if g.user is not None and g.user.is_authenticated:
        flash('You are already signed in')
        return redirect(url_for('home'))

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
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
            return redirect(url_for(signup))
        elif request.form['password'] != request.form['confirm_password']:
            flash('The passwords do not match')
            return redirect(url_for(signup))
        else:
            user = User(request.form['first_name'], request.form['last_name'], request.form['email'], generate_password_hash(request.form['password']))
            db.session.add(user)
            db.session.commit()
        if user != None:
                login_user(user)
        return redirect(url_for('home'))
    else:
        return render_template('signup.html', form = form)

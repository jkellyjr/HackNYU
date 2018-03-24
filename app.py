#********************************** IMPORTS  **********************************
from HACKNYU2018Github import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, g
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, RememberTopic, Crisis
from .forms import LoginForm, SignUpForm
<<<<<<< HEAD
from .phone import SMS

=======
#from .phone import SMS
from datetime import date
>>>>>>> b3ce4fb4e7cea56a0035a799c377066875aeb742

#********************************** HELPERS  **********************************
@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = date.today()
        db.session.add(g.user)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#********************************** VIEWS  **********************************
@app.route('/', methods = ['GET'])
@login_required
def home():
    flash("Glad to hear from you " + g.user.first_name)

    user = User.query.filter_by(id = g.user.id).first()

    if user.user_role == 'patient':
        headers = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return render_template('index.html', user = g.user, table_head = headers, remeber_topics = user.remember_topics)
    else:
        patients = User.query.filter(User.therapist.any(id = g.user.id)).all()
        return render_template('index.html', user = g.user, patients = patients)


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
    session.pop('_flashes', None)
    return redirect(url_for('login'))


@app.route('/new_topic', methods = ['GET', 'POST'])
def add_remeber_topic():
    if request.method == 'POST':
        topic = RememberTopic(request.form['topic_title'], g.user.id)
        db.session.add(topic)
        db.session.commit()
        return redirect(url_for('home'))


# TODO
@app.route('/rate_day/<rating>', methods = ['GET', 'POST'])
def rate_day(rating = None):
    if request.method == 'POST' and rating != None:
        print("day rating: " + str(rating))
    return redirect(url_for('home'))


# TODO
@app.route('/crisis', methods = ['GET', 'POST'])
def crisis():
    crisis = Crisis.query.filter(Crisis.type == 'panic_attack').first()
    steps = [step for step in crisis.steps]
    print(crisis.steps)

    return render_template('crisis.html', steps = steps)


@app.route('/contact', methods = ['GET', 'POST'])
def contact_professionsal():
    message = "hello friend, I'm having a crisis and i need help"
    SMS.emergency_message(message)
    return redirect(url_for('home'))


@app.route('/patient/<p_id>', methods = ['GET'])
def patient_sched(p_id):
    user = User.query.filter_by(id = p_id).first()

    headers = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('index.html', user = user, table_head = headers, remeber_topics = user.remember_topics)


#TODO
@app.route('/search', methods = ['GET', 'POST'])
def search_for_therapists():
    users = User.query.filter_by(user_role = 'therapist').all()
    return render_template('search_results.html', results = users)


<<<<<<< HEAD

=======
#TODO
>>>>>>> b3ce4fb4e7cea56a0035a799c377066875aeb742
@app.route('/update_table', methods = ['POST'])
def update_table():
    print("poster called")
    print(request.form['value'])
    return redirect(url_for('home'))



<<<<<<< HEAD

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    return render_template('profile.html')

=======
@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    user = User.query.filter_by(id = g.user.id).first()
    return render_template('profile.html', user = user)
>>>>>>> b3ce4fb4e7cea56a0035a799c377066875aeb742

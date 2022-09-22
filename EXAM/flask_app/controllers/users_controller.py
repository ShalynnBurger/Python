from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.car_model import Car
bcrypt = Bcrypt(app)

#homepage
@app.route('/')
def index():
    return render_template('index.html')

#register new user
@app.route('/users/register', methods=['post'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : hashed_pass
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/welcome')

#login existing user
@app.route('/users/login', methods=['post'])
def login():
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid login info a', 'log')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid login info b', 'log')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/welcome')

#logout
@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')

#personal homepage
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_cars = Car.get_all()
    user_data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(user_data)
    return render_template( 'dashboard.html', all_cars=all_cars, logged_user=logged_user )
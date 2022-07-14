from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/users')
def all_users():
    all_users = User.get_all()
    return render_template('read.html', all_users = all_users);

@app.route('/users/new')
def create_user():
    return render_template('create.html')

@app.route('/users/submit', methods=['post'])
def submit_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.save(data)
    return redirect('/users')
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/users')
def all_users():
    all_users = User.get_all()
    return render_template('read.html', all_users = all_users)

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

@app.route('/users/<id>')
def show_user(id):
    data = {
        'id': id
    }
    user_data = User.find_user(data)
    print(user_data)
    return render_template('show_user.html', user_data = user_data)

@app.route('/users/edit/<id>')
def edit_user(id):
    data = {
        'id': id
    }
    user_data = User.find_user(data)
    print(user_data)
    return render_template('edit.html', user_data = user_data)

@app.route('/users/edit/submit/<id>', methods=['post'])
def submit_edit(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    User.update_user(data)
    return redirect(f'/users/{id}')

@app.route('/users/delete/<id>')
def delete_user(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/users')
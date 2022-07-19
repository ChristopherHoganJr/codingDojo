from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.form import Form
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    if 'user_id' in session:
        session.clear()
    return render_template('index.html')

@app.route('/add', methods=['post'])
def add_user():
    if not Form.validate_form(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
    }
    result = Form.check_email_db(data)
    if len(result) < 1:
        user_id = Form.create_new_user(data)
        print(f'User Added with id of {user_id}!')
        session['user_id'] = user_id
        return redirect('/success')
    else:
        flash('That email already exists')
        return redirect('/')

@app.route('/users/login', methods=['post'])
def login_user():
    print(request.form['email'])
    print(request.form['password'])
    data = {
        'email': request.form['email']
    }
    user_in_db = Form.get_user_by_email(data)
    print(user_in_db.password)
    if not user_in_db:
        flash('Invalid email/password')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email/password')
        return redirect('/success.html')

    session['user_id'] = user_in_db.id
    print(session['user_id'])
    return redirect('/success')

@app.route('/success')
def success_page():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user_in_db = Form.get_one_by_id(data)
    return render_template('/success.html', user_in_db=user_in_db)
from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.User import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

# Home Page
@app.route('/')
def login_page():
    if 'user_id' in session:
        del session['user_id']
    return render_template('login.html')

# Have user sign up
@app.route('/user/register', methods=['post'])
def create_new_user():
    if not User.validate_form(request.form):
        return redirect('/')
    
    user_in_db = User.get_user_by_email({'email':request.form['email']})
    print(user_in_db)
    if user_in_db:
        flash('That email already exists')
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
    user_id = User.create_new_user(data)
    print(f'User Added with id of {user_id}!')
    session['user_id'] = user_id
    return redirect('/recipes')


# Login if user has an account
@app.route('/users/login', methods=['post'])
def login_user():
    user_in_db = User.get_user_by_email({'email': request.form['email']})

    if not user_in_db:
        flash('Invalid email/password fail one')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login-password']):
        flash('Invalid email/password password is wrong')
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/recipes')


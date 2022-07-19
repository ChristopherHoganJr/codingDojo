from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.validator import Validator

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['post'])
def add_email():
    if not Validator.validate_email(request.form):
        return redirect('/')
    data = {
        'email': request.form['email']
    }
    result = Validator.check_email(data)
    if len(result) < 1:
        Validator.add(data)
        return redirect('/success')
    else:
        flash('That email already exists')
        return redirect('/')

@app.route('/success')
def success():
    emails = Validator.get_emails()
    return render_template('success.html', emails = emails)

@app.route('/delete/<id>')
def delete_email(id):
    data = {
        'id': id
    }
    Validator.delete(data)
    return redirect('/success')
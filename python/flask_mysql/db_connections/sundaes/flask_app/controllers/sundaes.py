print('Running Controller File')
from flask_app import app
from flask import render_template, redirect, session, request
# import model
from flask_app.models.sundae import Sundae

@app.route('/')
def index():
    all_sundaes = Sundae.get_all()
    return render_template('index.html', all_sundaes=all_sundaes)

@app.route('/sundaes/create')
def create_form():
    return render_template('create_form.html')

@app.route('/sundaes/submit', methods=['post'])
def submit_sundae():
    # print('submitted!')
    # for key in request.form:
    #     print(f'{key}: {request.form[key]}')
    # Sundae.save(request.form)
    data = {
        'flavor': request.form['flavor'],
        'sauce': request.form['sauce'],
        'topping1': request.form['topping1'],
        'topping2': request.form['topping2'],
        'container': request.form['container'],
        'scoops': request.form['scoops']
    }
    Sundae.save(data)
    return redirect('/')
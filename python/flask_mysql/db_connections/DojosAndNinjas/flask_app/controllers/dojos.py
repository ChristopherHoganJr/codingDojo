from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', all_dojos = all_dojos)

@app.route('/dojos/add', methods=['post'])
def add_new_dojo():
    data = {
        'name': request.form['dojo_name']
    }
    Dojo.create_new_dojo(data)
    return redirect('/dojos')

@app.route('/ninjas')
def dojo_list():
    all_dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html', all_dojos = all_dojos)

@app.route('/dojos/<id>')
def dojo_show(id):
    data = {
        'id': id
    }
    dojo_info = Dojo.show_ninjas_in_dojo(data)

    return render_template('dojo_show.html', dojo_info = dojo_info)
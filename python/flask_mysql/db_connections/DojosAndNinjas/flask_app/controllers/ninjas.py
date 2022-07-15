from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.ninja import Ninja

@app.route('/ninjas/add_new', methods=['post'])
def add_new_ninja():
    data = {
        'first_name': request.form['ninja_fname'],
        'last_name': request.form['ninja_lname'],
        'age': request.form['ninja_age'],
        'dojo_id': request.form['ninja_dojo'],
    }
    Ninja.create_new_ninja(data)
    return redirect('/dojos')
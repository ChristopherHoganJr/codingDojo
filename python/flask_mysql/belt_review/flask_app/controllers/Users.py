from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.User import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def login_page():
    return render_template('all_recipes.html')
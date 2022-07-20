from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.Recipe import Recipe
from flask_app.models.User import User

@app.route('/recipes')
def recipes_main():
    if 'user_id' not in session:
        return redirect('/')

    user_in_db = User.get_one_by_id({'id':session['user_id']})
    print(user_in_db)
    all_recipes = Recipe.get_all_with_users()
    return render_template('all_recipes.html', user_in_db = user_in_db, all_recipes=all_recipes)

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/recipes/new/submit', methods=['post'])
def add_new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    user_in_db = User.get_one_by_id({'id':session['user_id']})
    data = {
        'name':request.form['name'],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'date':request.form['date'],
        'under_30':request.form.getlist('under_30'),
        'user_id':user_in_db.id
    }
    if not Recipe.validate_recipe(data):
        return redirect('/recipes/new')


    
    # Recipe.create_new_recipe(data)    
    return redirect('/recipes')

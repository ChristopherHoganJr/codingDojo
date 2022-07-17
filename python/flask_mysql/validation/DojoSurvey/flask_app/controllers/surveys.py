from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.survey import Survey

@app.route('/')
def index_form():
    return render_template('index.html')

@app.route('/results/add', methods=['post'])
def result_form():
    if not Survey.validate_survey(request.form):
        return redirect('/')

    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment'],
    }
    
    Survey.create_new_info(data)
    return redirect('/results/show')

@app.route('/results/show')
def show_results():
    survey_result = Survey.get_last_entry()
    return render_template('results.html', survey = survey_result[0])
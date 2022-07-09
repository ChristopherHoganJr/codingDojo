from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'asdf'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['userStats'] = request.form
    print(session['userStats'])
    return redirect('/result/display')

@app.route('/result/display')
def displayResults():
    return render_template('result.html', stats = session['userStats'])

@app.route('/')
def getHome():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
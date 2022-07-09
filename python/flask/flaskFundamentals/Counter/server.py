from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'asdf'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counter():
    session['counter'] += int(request.form['countSelector'])
    return render_template('index.html')

@app.route('/destory_session', methods=['POST'])
def destorySession():
    session.pop('counter')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
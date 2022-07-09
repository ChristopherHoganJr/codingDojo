from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'asdf'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counter():
    clicks = int(request.form)
    return 

if __name__=='__main__':
    app.run(debug=True)
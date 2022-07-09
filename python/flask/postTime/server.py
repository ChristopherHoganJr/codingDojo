from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# session needs secret key
app.secret_key = "it's a secret to everybody"

@app.route('/')
def sundae_form():
    return render_template('index.html')

@app.route('/sundaes/submit', methods=['POST'])
def submit_sundae():
    # Redirect is a better return
    #return render_template('display.html', sundae=request.form)
    print('going to submit')
    session['sundae'] = request.form
    return redirect('/sundaes/display')

@app.route('/sundaes/display')
def display():
    print('going to sundaes display')
    return render_template('displayAN.html', sundae=session['sundae'])



if __name__ == '__main__':
    app.run(debug=True)
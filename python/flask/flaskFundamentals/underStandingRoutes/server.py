from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:wordToSay>')
def say(wordToSay):
    return f'Hi {wordToSay.capitalize()}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeatWord(num,word):
    return word*num

@app.errorhandler(404)
def pageError(e):
    return 'Sorry! No response. Try again'

if __name__=='__main__':
    app.run(debug=True)
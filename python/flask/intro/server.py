# Importing Flask
from flask import Flask, render_template
# create variable called app - start flask server
app = Flask(__name__)

# Routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello")
def hello_page():
    return "yoooooo, it's the hello page!!!"

@app.route("/repeat/<phrase>")
def repeat_phrase(phrase):
    return f'your phrase is: {phrase}'

# int:variable will make the variable data type an int
#@app.route("/repeat/<phrase>/<int:times>")
#def repeat_times(phrase, times):
#    return (phrase + " ") * times

if __name__ == "__main__":
    app.run(debug=True)
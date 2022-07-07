from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the home page'

@app.route('/play')
def boxes():
    return render_template('index.html',boxes=3)

@app.route('/play/<int:numBoxes>')
def boxesNum(numBoxes):
    return render_template('index.html',boxes=numBoxes)

@app.route('/play/<int:numBoxes>/<string:boxColor>')
def boxNumColor(numBoxes, boxColor):
    return render_template('index.html',boxes=numBoxes,boxColor=boxColor)

@app.errorhandler(404)
def pageError(e):
    return 'this page doenst exist yet'

if __name__=='__main__':
    app.run(debug=True)
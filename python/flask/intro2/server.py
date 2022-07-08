from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<name>/<color>/<int:times>')
def index(name,color,times):
    return render_template('index.html', name=name, color=color, times=times)

if __name__=='__main__':
    app.run(debug=True)
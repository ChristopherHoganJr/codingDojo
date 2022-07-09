from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'the secret key'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    totalItems = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    session['totalItems'] = totalItems
    session['form'] = request.form
    print(f"Charging {request.form['first_name']} for {totalItems} fruits")
    #return render_template("checkout.html", order=request.form, totalItems = totalItems)
    return redirect('/SessionCheckout')

@app.route('/SessionCheckout')
def showCheckout():
    return render_template("checkout.html", order = session['form'], totalItems = session['totalItems'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
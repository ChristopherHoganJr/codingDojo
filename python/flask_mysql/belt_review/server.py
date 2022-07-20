from flask_app import app
from flask_app.controllers import Users
from flask_app.controllers import Recipes

if __name__ == '__main__':
    app.run(debug = True)
print('Running Server File')

from flask_app import app
# controller
from flask_app.controllers import sundaes

if __name__ == '__main__':
    app.run(debug = True)
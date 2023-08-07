#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB! to the route / """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB to the route /hbnb """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

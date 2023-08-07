#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ returns Hello HBNB! to the route / """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ returns HBNB to the route /hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ returns C <text> to the route /c/<text> """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def py(text):
    """will return python <text> tothe route /python/<text>"""
    return ("Python {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

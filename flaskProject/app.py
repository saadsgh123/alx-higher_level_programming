from email.policy import default

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/user/<name>')
def show_user_profile(name):
    return f'Hello {name}'


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_root(text):
    """ def doc """
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask
from json import dumps

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return dumps({'test_resp': 'Hello world!'})


if __name__ == '__main__':
    app.run()

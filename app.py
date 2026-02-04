from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Robert Smith! This is my first HTML page.'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)

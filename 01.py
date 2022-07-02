from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello,World"


@app.route("/member/<name>")
def hello_member(name):
    return f"Hello, {name}"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
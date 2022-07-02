from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello,World"

@app.route("/owner")
def owner():
    return "Hello Owner"

@app.route("/owner/<name>")
def owner_name(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
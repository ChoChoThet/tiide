from flask import Flask

app = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello World"

@myapp.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"

@myapp.route("/chothet")
def chothet():
    return "Cho Cho Thet"

if __name__ == "__main__":
    app.run()

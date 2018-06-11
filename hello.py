from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"

@app.route("/chothet")
def chothet():
    return "Cho Cho Thet"

if __name__ == "__main__":
    app.run()

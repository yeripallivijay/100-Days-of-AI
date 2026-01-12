from flask import Flask

##WSGL Application-1
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this 100 days journey"

@app.route("/index")
def index():
    return "Welcome to the index page "

if __name__ == "__main__":
    app.run(debug=True)
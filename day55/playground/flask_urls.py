from flask import Flask

app = Flask(__name__)

# app.route() decorator creates paths


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def Bye():
    return "Bye"

# <> surrounds variable path names converter uses a colon to seperate a type and variable name


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f" Hello, {name}. You are {number} years old!"


# include debug=Truee in order to avoid loading server after changes or to debug issues
if __name__ == "__main__":
    app.run(debug=True)

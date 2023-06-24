from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}<b/>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper
# include html/css elements in function to style


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
        "<p>This is a paragraph</p>" \
        "<img src='https://media1.giphy.com/media/LOcDU7Y6KBYTbG6eqd/giphy.gif' width=400>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)

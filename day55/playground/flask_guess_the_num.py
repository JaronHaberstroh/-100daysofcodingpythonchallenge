import random
from flask import Flask

ran_num = random.randint(0, 9)

app = Flask(__name__)


def is_higher_lower(function):
    def wrapper(num):
        if num == ran_num:
            function(num)
            return "You guessed it!<br>" \
                "<img src='https://media3.giphy.com/media/iowmvjVUnDFGU/200w.webp?cid=ecf05e47l1ei656z5hup210kltnd0xxdp7rjcz80e8bxtmx3&ep=v1_gifs_search&rid=200w.webp&ct=g'>"
        if num < ran_num:
            function(num)
            return f"{num} is less than number. Guess again.<br>" \
                "<img src='https://media1.giphy.com/media/oEnTTI3ZdK6ic/giphy.webp?cid=ecf05e47vx4fnhqg3gpinkoswtj7qobyg4gnevxlulq9pfza&ep=v1_gifs_search&rid=giphy.webp&ct=g'>"
        if num > ran_num:
            function(num)
            return f"{num} is greater than number. Guess again.<br>" \
                "<img src='https://media3.giphy.com/media/YsTs5ltWtEhnq/200w.webp?cid=ecf05e478hyvnonmkrl8e6m8g1hdyszunjj4l3j3qka5xqe5&ep=v1_gifs_search&rid=200w.webp&ct=g'>"
    return wrapper


@app.route("/")
def home():
    return "Can you guess the number (0-9)<br>" \
        "<img src='https://media4.giphy.com/media/y65VoOlimZaus/200.webp?cid=ecf05e47jq6majq3i74kxpzbolyy2j3gzb4jkyjg8hettvu9&ep=v1_gifs_search&rid=200.webp&ct=g'><br>" \
        "Complete challenge by typing guess into the address bar"


@app.route("/<int:num>")
@is_higher_lower
def num_guess(num):
    return num


if __name__ == "__main__":
    app.run(debug=True)

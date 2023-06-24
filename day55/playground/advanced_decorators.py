# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return "Home"

# if __name__ == "__main__":
#     app.run(debug=True)

class User():
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in is True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Jaron")
new_user.is_logged_in = True
create_blog_post(new_user)

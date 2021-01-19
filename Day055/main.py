from flask import Flask
app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1>Hello, World!<h1>' \
        '<p> Something </p>'

@app.route('/path/<path>')
def hello_world2(path):
    return 'Hello, World!' + path

@make_bold
@make_underlined
@make_emphasis
def test():
    return "Marcelo"



# if __name__ == '__main__':
#     print(test())
#     app.run(debug=True)

#==================================
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
    

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Marcelo")
create_blog_post(new_user) #Do nothing because decorator
new_user.is_logged_in= True
create_blog_post(new_user)
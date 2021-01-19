from flask import Flask
import random



app = Flask(__name__)

number = 0

@app.route('/')
def home():
    global number
    number = random.randint(0,9)
    html = """
    <center>
    <h1>Guess a number between 0 and 9</h1>
    <br>
    <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='200'>
    </center>
    """
    return html

@app.route('/<int:n>')
def get_value(n):
    if n == number:
        message = "You Found me!"
        image = "https://media.giphy.com/media/nN0NhNYVkdMkM/giphy.gif"
    elif n > number:
        message = "Too high, try again!"
        image = "https://media.giphy.com/media/60rUVyj8ShyuEhHbaz/giphy.gif"
    elif n < number:
        message = "Too low, try again!"
        image = "https://media.giphy.com/media/nR4L10XlJcSeQ/giphy.gif"
    
    return f"""
    <h1>{message}<h1>
    <br>
    <img src='{image}'>
    """

if __name__ == '__main__':
    app.run(debug=True)
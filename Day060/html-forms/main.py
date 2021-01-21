from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def receive_data():
    if request.method == 'POST':
        return f"<h1>UserName: {request.form['username']}, Password: {request.form['password']}</h1>"
    else:
        return "<h1>Please you need to login </h1>"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
import random, datetime, requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", num=random.randint(0,200), year=datetime.datetime.now().year)

@app.route('/guess/<name>')
def guess(name):
    name = name.strip().split()[0]
    gender = requests.get("https://api.genderize.io?name="+name).json()['gender']
    age = requests.get("https://api.agify.io/?name="+name).json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    #https://www.npoint.io/
    #this website creates a json and publish it to web
    blog = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
    return render_template("blog.html", posts=blog)



if __name__ == '__main__':
    app.run(debug=True)

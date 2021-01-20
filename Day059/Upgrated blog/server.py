from flask import Flask, render_template
import random, datetime, requests


app = Flask(__name__)
blog = None

@app.route('/')
def index():
    global blog
    blog = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
    return render_template("index.html", posts=blog)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def get_post(post_id):
    global blog
    if blog is None:
        blog = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
    final_article = {
        "id":post_id, 
        "body": "Post not found", 
        "title": "Post not found",
        "subtitle":"Post not found"
    }
    for artitle in blog:
        if artitle['id'] == post_id:
            final_article = artitle
    return render_template("post.html", post=final_article)

if __name__ == '__main__':
    app.run(debug=True)
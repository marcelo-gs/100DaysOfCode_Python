from flask import Flask, render_template
import requests

app = Flask(__name__)
blog = None

@app.route('/')
def home():
    global blog
    blog = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
    return render_template("index.html", posts=blog)

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    global blog
    if blog is None:
        blog = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
    final_article = {
        "id":blog_id, 
        "body": "Post not found", 
        "title": "Post not found",
        "subtitle":"Post not found"
    }
    for artitle in blog:
        if artitle['id'] == blog_id:
            final_article = artitle
    return render_template("post.html", post=final_article)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import random, datetime, requests, smtplib


app = Flask(__name__)
blog = None

OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"

@app.route('/')
def index():
    global blog
    blog = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
    return render_template("index.html", posts=blog)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

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


def send_email(name, email, phone, message):
    email_message = f"Subject:New Contact\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

#on Chrome developer tools => Console
#document.body.contentEditable=true
#To do this make the page editable from the brownser
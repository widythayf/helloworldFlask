from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    #return "<h2>Hello World! I'm using Flask.</h2>"
    return render_template("home.html")
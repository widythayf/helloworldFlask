from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
css = Bundle("src/input.css", output="dist/output.css")

assets.register("css", css)
css.build()

@app.route("/")
def home():
    #return "<h2>Hello World! I'm using Flask.</h2>"
    #return render_template("home.html")
    return render_template("helloworld.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
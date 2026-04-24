from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create")
def create():
    return render_template("index.html")


@app.route("/solve")
def solve():
    return render_template("solve.html")

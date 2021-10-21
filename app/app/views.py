from flask import render_template

from . import app


@app.route("/")
def hello_world():
    return render_template("main.html")

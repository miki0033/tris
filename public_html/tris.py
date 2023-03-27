import os
def clear():
    os.system("cls")
# -----------
from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import abort, redirect, url_for
# -----------

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/homepage")
def home():
    return render_template("homepage.html")


# -----------
clear()

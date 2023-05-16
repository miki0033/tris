# -----------import Lib-----------
import os
from tris_lib import trislib
import classi

import random

# -----------import Flask Lib-----------
from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import abort, redirect, url_for
from flask import request
from flask import session
from flask import json

# -----------import Database-----------
from flask_mysqldb import MySQL
import MySQLdb.cursors

import pw
import re  # lib per check sulle regex
import sys  # serve per debug


app = Flask(__name__)
app.secret_key = pw.SECRET_KEY

# DB config
app.config["MYSQL_HOST"] = pw.DBHOST
app.config["MYSQL_USER"] = pw.DBUSER
app.config["MYSQL_PASSWORD"] = pw.DBPW
app.config["MYSQL_DB"] = pw.DB

mysql = MySQL(app)
import db

if __name__ == "__main__":
    app.run(debug=True)


# -----------Flask code-----------
app = Flask(__name__)
# Chiave di salatura(non dovrebbe essere publica)
app.secret_key = pw.SECRET_KEY


# ROUTE
@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/homepage")
def home():
    return render_template("homepage.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
    ):
        username = request.form["username"]
        email = request.form["email"]
        password = pw.pwEncode(password)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM utenti WHERE email = % s", (email,))
        account = cursor.fetchone()
        if account:
            msg = "Email already registered, plase Log in!"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address !"
        elif not username or not password or not email:
            msg = "Please fill out the form !"
        else:
            cursor.execute(
                "INSERT INTO utenti VALUES (NULL, % s, % s, % s, % s, NULL, NULL)",
                (username, email, password),
            )
            mysql.connection.commit()  # salva i dati nel database
            msg = "You have successfully registered !"
            return redirect(url_for("login"))
    elif request.method == "POST":
        msg = "Please fill out the form !"
    return render_template("register.html", msg=msg)


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        password = pw.pwEncode(password)
        # l' oggetto cursor ritorna le righe del database come dizionari
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # execute esegue la query
        cursor.execute(
            "SELECT * FROM utenti WHERE username = % s AND password = % s",
            (
                username,
                password,
            ),
        )
        # fetchone() ritorna la prossima riga della tabella, se si è arrivati alla fine ritorna None
        account = cursor.fetchone()
        if account:
            session["loggedin"] = True
            session["id"] = account["id"]
            session["username"] = account["username"]

            msg = "Logged in successfully !"
            return redirect(url_for("home"))
        else:
            msg = "Incorrect username or password!"
    return render_template("login.html", msg=msg)


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect(url_for("login"))


# API
@app.route("/new_room", methods=["GET"])
def __init__():
    # Inizializza la stanza
    if logCheck():
        username = session["username"]  # recupera l'username dell'utente
    else:
        username = "Guest" + str(random.randint(1000, 9999))
        session["username"] = username
    room = classi.TrisRoom(username)
    codiceStanza = room.getRoomCode()

    return redirect(f"/{codiceStanza}/{username}", avatar="X")


@app.route("/join", methods=["GET", "POST"])
def join():
    # Fa in modo di entrare in una stanza già esistente
    if logCheck():
        username = session["username"]  # recupera l'username dell'utente
    else:
        username = "Guest" + str(random.randint(1000, 9999))
        session["username"] = username

    codiceStanza = request.form["join"]
    if classi.ActiveRooms.checkCode(codiceStanza):
        p_room = classi.ActiveRooms.getRoom()
        classi.TrisRoom.joinRoom(
            p_room, username
        )  # controllo sul numero di utenti nella stanza

        for i in p_room.giocatori:
            trislib.printTerminal(i)
    return redirect(f"/{codiceStanza}/{username}", avatar="O")


@app.route("/<string:codiceStanza>/<string:username>", methods=["GET", "POST"])
def tris(codiceStanza, username):
    # controlla la mossa effettuata
    # salva la mossa se è valida
    # scambia la variabile del turno
    return render_template("tris.html", codiceStanza=codiceStanza, username=username)


@app.route("/<string:codiceStanza>", methods=["GET"])
def getStatus(codiceStanza):
    # Ritorna un array JSON con lo stato della partita(casselle occupate, di chi è il turno)
    # Richimare tramite Javascript
    if classi.ActiveRooms.checkCode(codiceStanza):
        p_room = classi.ActiveRooms.getRoom()
        mossa = classi.TrisRoom.getMove(p_room)
        response = app.response_class(
            response=json.dumps(mossa), status=200, mimetype="application/json"
        )
    else:
        response = app.response_class(
            response=json.dumps(), status=404, mimetype="application/json"
        )

    return response


@app.route("/mossa/<string:codiceStanza>/<string:username>", methods=["GET"])
def setStatus(codiceStanza):
    # Ritorna un array JSON con lo stato della partita(casselle occupate, di chi è il turno)
    # Richimare tramite Javascript
    json = ""
    return json


# ---------FUNCIONS------------


def logCheck():
    # controlla che l'utente sia loggato
    # restituisce true se l'utente è loggato, false altrimenti
    if "username" in session:
        return True
    else:
        return False


# -----------MAIN-----------
# trislib.clearTerminal()

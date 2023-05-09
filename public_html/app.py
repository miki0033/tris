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


# -----------Flask code-----------
app = Flask(__name__)
# Chiave di salatura(non dovrebbe essere publica)
app.secret_key = b"f6c23211b07568ace2707f28180429677fe1b34d6b1ba04a6114243781fbd4f2"


# ROUTE
@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/homepage")
def home():
    return render_template("homepage.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


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

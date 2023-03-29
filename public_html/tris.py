# -----------import Lib-----------
import os
from public_html.tris_lib import trislib
import classi
# -----------import Flask Lib-----------
from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import abort, redirect, url_for
# -----------Flask code-----------

app = Flask(__name__)

# ROUTE


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/homepage")
def home():
    return render_template("homepage.html")


# API

@app.route('/new_room', methods=['GET'])
def __init__():
    # TODO: bisogna recuperare l'username dell'utente in qulche modo

    # Inizializza la stanza
    room = classi.TrisRoom(username)
    codiceStanza = room.getRoomCode()
    return redirect(f'/{codiceStanza}/{username}')


@app.route('/join/<str:codiceStanza>', methods=['GET'])
def join():
    # Fa in modo di entrare in una stanza già esistente
    # controllo sul numero di utenti nella stanza
    # <2 accedi alla stanza come giocatore
    # >2 accedi alla stanza come spettatore
    return redirect('/codice_stanza/n_utente')


@app.route('/<string:codiceStanza>/<string:username>', methods=['POST'])
def mossa():
    # controlla la mossa effettuata
    # salva la mossa se è valida
    # scambia la variabile del turno
    return


@app.route('/<str:codiceStanza>', methods=['GET'])
def getStatus():
    # Ritorna un array con lo stato della partita(casselle occupate, di chi è il turno)

    return


# -----------MAIN-----------
trislib.clearTerminal()

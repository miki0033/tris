# -----------import Lib-----------
import os
from tris_lib import trislib
import classi
# -----------import Flask Lib-----------
from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import abort, redirect, url_for
from flask import request
from flask import session
# -----------Flask code-----------
app = Flask(__name__)
# Chiave di salatura(non dovrebbe essere publica)
app.secret_key = b'f6c23211b07568ace2707f28180429677fe1b34d6b1ba04a6114243781fbd4f2'


# ROUTE
@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/homepage")
def home():
    return render_template("homepage.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session["username"] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')

# API
@app.route('/new_room', methods=['GET'])
def __init__():
    # Inizializza la stanza
    username = session["username"]  # recupera l'username dell'utente
    room = classi.TrisRoom(username)
    codiceStanza = room.getRoomCode()
    return redirect(f'/{codiceStanza}/{username}')


@app.route('/join/<string:codiceStanza>', methods=['GET'])
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


@app.route('/<string:codiceStanza>', methods=['GET'])
def getStatus():
    # Ritorna un array JSON con lo stato della partita(casselle occupate, di chi è il turno)
    # Richimare tramite Javascript

    return

# ---------FUNCIONS------------


def logCheck():
    # controlla che l'utente sia loggato
    # restituisce true se l'utente è loggato, false altrimenti
    if 'username' in session:
        return True
    else:
        return False


# -----------MAIN-----------
trislib.clearTerminal()

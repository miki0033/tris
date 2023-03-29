import random
import time
from public_html.tris_lib import trislib


class TrisRoom:
    # Campi
    codiceStanza = ""
    timestamp = 0
    giocatori = []
    spettatori = []

    # Metodi
    def __init__(self, host):
        self.giocatori.push(host)
        self.timestamp = time.timestamp()
        self.codiceStanza = self.createCode()

    @staticmethod
    def createCode():
        # idea:generare un codice tramite conversione in alfanumerico di un numero random/ o del timestamp
        flag = True  # true fin quando il codice non è valido
        rnd = time.timestamp()
        while (flag):
            code = trislib.convertB16(rnd)
            # check sui dati in tabella activeRoom
            flag = activeRoom.checkCode()

    def getRoomCode(self):
        return self.codiceStanza


class ActiveRoom:
    @staticmethod
    active = []  # array di oggetti TrisRoom

    def checkCode():
        # restituisce true se il codice è presente un tabella
        # false altrimenti

        result = False  # PROVVISORIO

        return result

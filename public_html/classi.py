# -----IMPORT-------
import random
import time

from datetime import datetime, timedelta

from public_html.tris_lib import trislib
# -----GLOBALI------
active = []  # array di oggetti TrisRoom
# -----Classi-------


class TrisRoom:
    # Campi
    codiceStanza = ""
    timestamp = 0
    timeout_time = 0
    giocatori = []
    spettatori = []

    # Metodi
    def __init__(self, host):
        self.giocatori.push(host)
        self.timestamp = datetime.now()
        self.timeout_time = timedelta(hours=1)
        self.codiceStanza = self.createCode()

    @staticmethod
    def createCode():
        # idea:generare un codice tramite conversione in alfanumerico di un numero random/ o del timestamp
        flag = True  # true fin quando il codice non è valido
        rnd = time.timestamp()
        while (flag):
            code = trislib.convertB16(rnd)
            # check sui dati in tabella activeRoom
            flag = ActiveRooms.checkCode(active)

    def getRoomCode(self):
        return self.codiceStanza

    def timeout(self):
        # restituisce true se è passato il tempo di timeout
        if (datetime.now() > self.timestamp+self.timeout_time):
            return True
        else:
            return False


class ActiveRooms:
    # sarebbe meglio mettere active come campo statico in python in modo da poterlo modificare solo tramite metodi
    # PROVVISORIO: active attualmente è globale

    def getActiveRooms(self):
        return self.active

    def pushRoom(self, pointer):
        self.active.push(pointer)

    def RoomTimeout(self):
        for i in self.active:
            if self.active[i].timeout():
                self.active.pop(i)

    @staticmethod
    def checkCode(self):
        # restituisce true se il codice è presente un tabella
        # false altrimenti

        result = False  # PROVVISORIO

        return result

# -----IMPORT-------
import random
from datetime import datetime, timedelta

from tris_lib import trislib

# -----GLOBALI------

# -----Classi-------


class TrisRoom:
    # Campi
    """
    codiceStanza = ""
    timestamp = 0
    timeout_time = 0
    """
    # giocatori = []
    host = ""
    guest = ""
    spettatori = []
    mosse = {
        "turn": "host",
        "NO": "",
        "N": "",
        "NE": "",
        "O": "",
        "C": "",
        "E": "",
        "SO": "",
        "S": "",
        "SE": "",
    }
    # Metodi

    def __init__(self, host):
        self.host = host
        self.timestamp = datetime.now()
        self.timeout_time = timedelta(hours=1)
        self.codiceStanza = TrisRoom.createCode()

        ActiveRooms.pushRoom(self)

    @staticmethod
    def createCode():
        # genera un codice tramite uuid
        flag = True  # true fin quando il codice non è valido
        while flag:
            rnd = random.randrange(100000, 1000000)
            # check sui dati in tabella activeRoom
            flag = ActiveRooms.checkCode(rnd)

    def getRoomCode(self):
        return self.codiceStanza

    def joinRoom(self, username):
        if not self.guest:
            self.guest = username
        else:
            self.spettatori.append(username)

    def getMove(self):
        return self.mosse

    def timeout(self):
        # restituisce true se è passato il tempo di timeout
        if datetime.now() > self.timestamp + self.timeout_time:
            return True
        else:
            return False


class ActiveRooms:
    # active come campo statico in python in modo da poterlo modificare solo tramite metodi
    active = []  # array di oggetti TrisRoom

    def getActiveRooms(self):
        return self.active

    def pushRoom(pointer):
        ActiveRooms.active.append(pointer)

    def RoomTimeout(self):
        for i in self.active:
            if TrisRoom.timeout(i):
                self.active.pop(i)

    @staticmethod
    def getRoom(code):
        for room in ActiveRooms.getActiveRooms():
            if room.codiceStanza == code:
                p = room
        return p

    @staticmethod
    def checkCode(code):
        # restituisce true se il codice è presente un tabella
        # false altrimenti
        result = False  # PROVVISORIO

        for i in ActiveRooms.active:
            if ActiveRooms.active[i].codiceStanza == code:
                result = True
        return result

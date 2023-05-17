# -----IMPORT-------
import random
from datetime import datetime, timedelta

from tris_lib import trislib
import uuid

# -----GLOBALI------

# -----Classi-------


class TrisRoom:
    # Campi
    """
    codiceStanza = ""
    timestamp = 0
    timeout_time = 0
    host = ""
    guest = ""
    spettatori = []
    mosse = {
        "turn": "X",
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
    """
    # Metodi

    def __init__(self, host):
        self.host = host
        self.guest = ""
        self.spettatori = []
        self.timestamp = datetime.now()
        self.timeout_time = timedelta(hours=1)
        self.codiceStanza = TrisRoom.createCode()
        self.mosse = {
            "turn": "X",
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
        ActiveRooms.pushRoom(self)

    @staticmethod
    def createCode():
        # genera un codice tramite uuid
        flag = True  # true fin quando il codice non è valido
        while flag:
            room_id = str(uuid.uuid4().hex)[:6]
            # check sui dati in tabella activeRoom
            flag = ActiveRooms.checkCode(room_id)
        return room_id

    def getRoomCode(self):
        return self.codiceStanza

    def joinRoom(self, username):
        if not self.guest:
            self.guest = username
            result = "guest"
        else:
            self.spettatori.append(username)
            result = "spectator"
        return result

    def assignedRole(self, username):
        if self.host == username:
            result = "host"
        elif self.guest == username:
            result = "guest"
        else:
            for user in self.spettatori:
                if user == username:
                    result = "spectator"
                else:
                    result = "error"
        return result

    def getMove(self):
        return self.mosse

    def setMove(self, mossa):
        if self.mosse["turn"] == "X":
            self.mosse["turn"] = "O"
        else:
            self.mosse["turn"] = "X"

        self.mosse["NO"] = mossa[0]
        self.mosse["N"] = mossa[1]
        self.mosse["NE"] = mossa[2]
        self.mosse["O"] = mossa[3]
        self.mosse["C"] = mossa[4]
        self.mosse["E"] = mossa[5]
        self.mosse["SO"] = mossa[6]
        self.mosse["S"] = mossa[7]
        self.mosse["SE"] = mossa[8]

    def timeout(self):
        # restituisce true se è passato il tempo di timeout
        if datetime.now() > self.timestamp + self.timeout_time:
            return True
        else:
            return False


class ActiveRooms:
    # active come campo statico in python in modo da poterlo modificare solo tramite metodi
    active = []  # array di oggetti TrisRoom

    @staticmethod
    def getActiveRooms():
        return ActiveRooms.active

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
        trislib.printTerminal(ActiveRooms.getActiveRooms())
        for room in ActiveRooms.active:
            trislib.printTerminal(room.codiceStanza)
            if room.codiceStanza == code:
                result = True
        return result

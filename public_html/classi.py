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
    """
    giocatori = []
    spettatori = []

    # Metodi

    def __init__(self, host):
        self.giocatori.push(host)
        self.timestamp = datetime.now()
        self.timeout_time = timedelta(hours=1)
        self.codiceStanza = self.createCode()

        ActiveRooms.pushRoom(self)

    @staticmethod
    def createCode():
        # genera un codice tramite uuid
        flag = True  # true fin quando il codice non è valido
        while (flag):
            room_id = str(uuid.uuid4().hex)[:6]
            # check sui dati in tabella activeRoom
            flag = ActiveRooms.checkCode(room_id)

    def getRoomCode(self):
        return self.codiceStanza

    def timeout(self):
        # restituisce true se è passato il tempo di timeout
        if (datetime.now() > self.timestamp+self.timeout_time):
            return True
        else:
            return False


class ActiveRooms:
    # active come campo statico in python in modo da poterlo modificare solo tramite metodi
    active = []  # array di oggetti TrisRoom

    def getActiveRooms(self):
        return self.active

    def pushRoom(pointer):
        ActiveRooms.active.push(pointer)

    def RoomTimeout(self):
        for i in self.active:
            if self.active[i].timeout():
                self.active.pop(i)

    @staticmethod
    def checkCode(code):
        # restituisce true se il codice è presente un tabella
        # false altrimenti
        result = False  

        for i in ActiveRooms.active:
            if ActiveRooms.active[i].codiceStanza == code:
                result = True

        return result
